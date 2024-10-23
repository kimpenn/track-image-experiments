import json, datetime
from django.db import models
from django.core.cache import cache

# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "species"


class Organs(models.Model):
    name = models.CharField(max_length=30, unique=True)


class OrganRegions(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "organ regions"


class People(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "people"


class StainingProtocols(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "staining protocols"


class ProbeTypes(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "probe types"


class FishTechnologies(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "fish technologies"


class FlourescentMolecules(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "flourescent molecules"


class ProbePanels(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "probe panels"


class ImagingSuccessOptions(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name_plural = "imaging success options"


"""
# not sure how to keep this from accessing the database when module is first imported
def get_choices(model):
    rows = model.objects.all()
    options = [row.name.strip() for row in rows]
    return list(zip(options, options))
"""


class Probe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    target_analyte = models.CharField(max_length=255)
    target_gencode_id = models.CharField(max_length=255, blank=True, default="")
    probe_type = models.ForeignKey(ProbeTypes, on_delete=models.SET_NULL, null=True, default=None)
    antibody_clone_id = models.CharField(max_length=30, blank=True, default="")
    fish_technology = models.ForeignKey(FishTechnologies, on_delete=models.SET_NULL, null=True, default=None)
    fluorescent_molecule = models.ForeignKey(FlourescentMolecules, on_delete=models.SET_NULL, null=True, default=None)
    stock_concentration = models.CharField(max_length=30, blank=True, default="")
    working_dilution = models.CharField(max_length=30, blank=True, default="")
    probe_panel = models.ForeignKey(ProbePanels, on_delete=models.SET_NULL, null=True, default=None)
    imaging_success = models.ForeignKey(ImagingSuccessOptions, on_delete=models.SET_NULL, null=True, default=None)
    staining_notes = models.TextField(blank=True, default="")
    imaging_notes = models.TextField(blank=True, default="")


class Panel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    probe_list = models.CharField(max_length=255, blank=True, default="")


class Microscope(models.Model):
    name = models.CharField(max_length=30, unique=True)
    model = models.CharField(max_length=30)
    json_description = models.FileField(upload_to="hardware_json/", blank=True, null=True)


class ExposureTime(models.Model):
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE)
    microscope = models.ForeignKey(Microscope, on_delete=models.CASCADE)
    exposure_time = models.DecimalField(decimal_places=4, max_digits=6)


class Donor(models.Model):
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
    sex = models.CharField(max_length=1, choices=SEX, default=UNKNOWN)
    age = models.PositiveSmallIntegerField(blank=True)

    class Meta:
        verbose_name_plural = "donor"


class Slides(models.Model):
    SLICE = "S"
    CULTURE = "C"
    SOURCE_FORMAT = {
        SLICE: "Slice",
        CULTURE: "Culture",
    }

    name = models.CharField(max_length=30, unique=True, default="")
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, default=None)
    organ = models.ForeignKey(Organs, on_delete=models.SET_NULL, null=True, default=None)
    organ_region = models.ForeignKey(OrganRegions, on_delete=models.SET_NULL, null=True, default=None)
    donor = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True, default=None)
    material_source = models.CharField(max_length=30, default="")
    source_format = models.CharField(max_length=1, choices=SOURCE_FORMAT, null=True, default=None)
    source_prep_by = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, default=None, related_name="source_prep_by"
    )
    source_prep_date = models.DateField(default=datetime.date.today)
    staining_protocol = models.ForeignKey(StainingProtocols, on_delete=models.SET_NULL, null=True, default=None)
    staining_by = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, default=None, related_name="staining_by"
    )
    staining_date = models.DateField(default=datetime.date.today)
    probe_panel = models.ManyToManyField(ProbePanels)
    imaging_by = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, default=None, related_name="imaging_by"
    )
    imaging_date = models.DateField(default=datetime.date.today)
    microscope = models.ForeignKey(Microscope, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        verbose_name_plural = "slides"
