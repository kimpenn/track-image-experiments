import json, datetime
from django.db import models
from django.core.cache import cache

# Create your models here.


class ModelWithName(models.Model):  # Abstract model, assuming a name field
    name = models.CharField(max_length=30, unique=True, blank=False, null=False)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.name)


class Species(ModelWithName):
    class Meta:
        verbose_name_plural = "species"


class Organs(ModelWithName):
    class Meta:
        verbose_name_plural = "organs"


class OrganRegions(ModelWithName):

    class Meta:
        verbose_name_plural = "organ regions"


class MaterialSources(ModelWithName):
    class Meta:
        verbose_name_plural = "material sources"


class SourceTreatments(ModelWithName):
    class Meta:
        verbose_name_plural = "source treatments"


class People(ModelWithName):
    class Meta:
        verbose_name_plural = "people"


class StainingProtocols(ModelWithName):
    class Meta:
        verbose_name_plural = "staining protocols"


class ProbeTypes(ModelWithName):
    class Meta:
        verbose_name_plural = "probe types"


class FishTechnologies(ModelWithName):
    class Meta:
        verbose_name_plural = "fish technologies"


class FlourescentMolecules(ModelWithName):
    class Meta:
        verbose_name_plural = "flourescent molecules"


class ImagingSuccessOptions(ModelWithName):
    class Meta:
        verbose_name_plural = "imaging success options"


class Panel(ModelWithName):
    description = models.CharField(max_length=255, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    # probe_list = models.CharField(max_length=255, blank=True, default="")


class Probe(ModelWithName):
    target_analyte = models.CharField(max_length=255)
    target_gencode_id = models.CharField(max_length=255, blank=True, default="")
    probe_type = models.ForeignKey(ProbeTypes, on_delete=models.SET_NULL, null=True, default=None)
    antibody_clone_id = models.CharField(max_length=30, blank=True, default="")
    fish_technology = models.ForeignKey(FishTechnologies, on_delete=models.SET_NULL, null=True, default=None)
    fluorescent_molecule = models.ForeignKey(FlourescentMolecules, on_delete=models.SET_NULL, null=True, default=None)
    stock_concentration = models.CharField(max_length=30, blank=True, default="")
    working_dilution = models.CharField(max_length=30, blank=True, default="")
    probe_panel = models.ManyToManyField(Panel, related_name="probes")
    imaging_success = models.ForeignKey(ImagingSuccessOptions, on_delete=models.SET_NULL, null=True, default=None)
    staining_notes = models.TextField(blank=True, default="")
    imaging_notes = models.TextField(blank=True, default="")


class Microscope(ModelWithName):
    model = models.CharField(max_length=30)
    json_description = models.CharField(
        max_length=50, blank=True, null=True, help_text="This file should exist in /lab/imaging/repo/resources/"
    )
    # json_description = models.FileField(upload_to="hardware_json/", blank=True, null=True)


class Source(models.Model):
    FEMALE = "F"
    MALE = "M"
    OTHER = "O"
    NOT_REPORTED = "N"
    UNKNOWN = "U"
    SEX = {
        FEMALE: "Female",
        MALE: "Male",
        OTHER: "Other",
        NOT_REPORTED: "Not reported",
        UNKNOWN: "Unknown",
    }

    lab_id = models.CharField(max_length=30, unique=True)
    public_id = models.CharField(max_length=30, blank=True, help_text="This could be the HuBMAP ID, if one exists.")
    public_id_source = models.CharField(
        max_length=80,
        blank=True,
        help_text="If a public ID is provided, then this is the organization where that ID is registered.",
    )
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, default=None)
    sex = models.CharField(max_length=1, choices=SEX, default=UNKNOWN)
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=None)

    # use "name" as alternative to "lab_id". this allows us to use our default foreign key display function in the admin panel
    @property
    def name(self):
        return self.lab_id

    class Meta:
        verbose_name_plural = "source"

    def __str__(self):
        return "{}".format(self.lab_id)


class Assay(models.Model):
    name = models.PositiveIntegerField(unique=True, blank=False, null=False, verbose_name="image ID")
    staining_protocol = models.ForeignKey(StainingProtocols, on_delete=models.SET_NULL, null=True, default=None)
    staining_by = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, default=None, related_name="staining_by"
    )
    staining_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    probe_panel = models.ManyToManyField(Panel, related_name="panels")
    imaging_by = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, default=None, related_name="imaging_by"
    )
    imaging_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    microscope = models.ForeignKey(Microscope, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        verbose_name_plural = "assays"


class Slide(ModelWithName):
    assay = models.ManyToManyField(Assay, related_name="assays")

    class Meta:
        verbose_name_plural = "slides"


class SliceOrCulture(ModelWithName):
    SLICE = "S"
    CULTURE = "C"
    SOURCE_FORMAT = {
        SLICE: "Slice",
        CULTURE: "Culture",
    }
    type = models.CharField(max_length=1, choices=SOURCE_FORMAT, null=True, default=None)
    parent = models.ForeignKey(
        Source,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        help_text="The donor for this tissue section, if relevant.",
    )
    organ = models.ForeignKey(Organs, on_delete=models.SET_NULL, null=True, default=None)
    organ_region = models.ForeignKey(OrganRegions, on_delete=models.SET_NULL, null=True, default=None)
    treatment = models.ForeignKey(SourceTreatments, on_delete=models.SET_NULL, null=True, default=None)
    storage_time = models.IntegerField(
        null=True, blank=True, help_text="How long was this stored before mounting (days)?"
    )
    prep_by = models.ForeignKey(
        People,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        related_name="source_prep_by",
        help_text="Who prepared this slice/culture?",
    )
    prep_date = models.DateField(
        default=datetime.date.today,
        null=True,
        blank=True,
        help_text="When was this slice/culture prepared?",
    )
    acquired_from = models.ForeignKey(
        MaterialSources,
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        help_text="Where did we get this material from?",
    )
    slide = models.ForeignKey(Slide, on_delete=models.SET_NULL, null=True, default=None)


class ExposureTime(models.Model):
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE)
    microscope = models.ForeignKey(Microscope, on_delete=models.CASCADE)
    exposure_time = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return "{} / {} / {} msec".format(self.probe, self.microscope, self.exposure_time)
