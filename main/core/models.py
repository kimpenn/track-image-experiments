import datetime
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


class ProbeVendor(ModelWithName):
    class Meta:
        verbose_name_plural = "probe vendors"


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
    protocol_filename = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        help_text="This file must exist in /lab/imaging/repo/resources/protocols",
    )

    class Meta:
        verbose_name_plural = "staining protocols"


class ProbeClasses(ModelWithName):
    class Meta:
        verbose_name_plural = "probe classes"


class ProbeTechnologies(ModelWithName):
    class Meta:
        verbose_name_plural = "probe technologies"


class CaptureChannel(ModelWithName):
    class Meta:
        verbose_name_plural = "capture channels"


class ImagingSuccessOptions(ModelWithName):
    class Meta:
        verbose_name_plural = "imaging success options"


class Probe(ModelWithName):
    target_analyte = models.CharField(max_length=255)
    target_ensembl_id = models.CharField(max_length=255, blank=True, default="")
    probe_class = models.ForeignKey(ProbeClasses, on_delete=models.SET_NULL, null=True, default=None)
    antibody_clone_id = models.CharField(max_length=30, blank=True, default="")
    probe_technology = models.ForeignKey(ProbeTechnologies, on_delete=models.SET_NULL, null=True, default=None)
    capture_channel = models.ForeignKey(CaptureChannel, on_delete=models.SET_NULL, null=True, default=None)
    stock_concentration = models.CharField(max_length=30, blank=True, default="")
    imaging_success = models.ForeignKey(ImagingSuccessOptions, on_delete=models.SET_NULL, null=True, default=None)
    staining_notes = models.TextField(blank=True, default="")
    imaging_notes = models.TextField(blank=True, default="")
    probe_vendor = models.ForeignKey(ProbeVendor, on_delete=models.SET_NULL, null=True, default=None)


class Panel(ModelWithName):
    description = models.CharField(max_length=255, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    probe = models.ManyToManyField(Probe, related_name="probes")


class Microscope(ModelWithName):
    model = models.CharField(max_length=30)
    json_filename = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="This file should exist in /lab/imaging/repo/resources/microscopes",
    )
    # json_description = models.FileField(upload_to="hardware_json/", blank=True, null=True)


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
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, default=None)
    sex = models.CharField(max_length=1, choices=SEX, default=UNKNOWN)
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=None)

    # use "name" as alternative to "lab_id". this allows us to use our default foreign key display function in the admin panel
    @property
    def name(self):
        return self.lab_id

    class Meta:
        verbose_name_plural = "donor"

    def __str__(self):
        return "{}".format(self.lab_id)


class Slide(models.Model):
    slide_id = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
        verbose_name="slide ID",
        help_text="This is an unique ID for the slide. It could, for example, be the Visium slide ID.",
    )

    # use "name" as alternative to "slide_id". this allows us to use our default foreign key display function in the admin panel
    @property
    def name(self):
        return self.slide_id

    def __str__(self):
        return "{}".format(self.slide_id)

    class Meta:
        verbose_name_plural = "slides"


class Assay(ModelWithName):
    staining_protocol = models.ForeignKey(StainingProtocols, on_delete=models.SET_NULL, null=True, default=None)
    panel = models.ManyToManyField(Panel, related_name="panels")

    class Meta:
        verbose_name_plural = "Assays"


class Image(models.Model):
    image_id = models.PositiveIntegerField(unique=True, blank=False, null=False, verbose_name="image ID")
    assay = models.ForeignKey(
        Assay, on_delete=models.SET_NULL, null=True, default=None, related_name="assays", blank=True
    )
    slide = models.ForeignKey(
        Slide, on_delete=models.SET_NULL, null=True, default=None, related_name="slides", blank=True
    )
    staining_by = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, default=None, related_name="staining_by"
    )
    staining_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    imaging_by = models.ForeignKey(
        People, on_delete=models.SET_NULL, null=True, default=None, related_name="imaging_by"
    )
    imaging_date = models.DateField(default=datetime.date.today, null=True, blank=True)
    microscope = models.ForeignKey(Microscope, on_delete=models.SET_NULL, null=True, default=None)

    # use "name" as alternative to "image_id". this allows us to use our default foreign key display function in the admin panel
    @property
    def name(self):
        return self.image_id

    def __str__(self):
        return "{}".format(self.image_id)

    class Meta:
        verbose_name_plural = "Images"


class Sample(models.Model):
    SLICE = "S"
    CULTURE = "C"
    SOURCE_FORMAT = {
        SLICE: "Slice",
        CULTURE: "Culture",
    }

    sample_id = models.CharField(
        max_length=30,
        unique=True,
        blank=True,
        null=True,
        verbose_name="sample ID",
        help_text="This is an unique ID for the sample.",
    )
    parent_id = models.CharField(
        max_length=30,
        unique=False,
        blank=False,
        null=False,
        verbose_name="parent ID",
        help_text="This is the ID for the source block or tissue used to derive this sample.",
    )
    type = models.CharField(max_length=1, choices=SOURCE_FORMAT, null=True, default=None)
    donor = models.ForeignKey(
        Donor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        help_text="The donor for this tissue section, if relevant.",
    )
    organ = models.ForeignKey(Organs, on_delete=models.SET_NULL, null=True, default=None)
    organ_region = models.ForeignKey(OrganRegions, on_delete=models.SET_NULL, null=True, default=None)
    thickness = models.PositiveIntegerField(
        null=True, blank=True, help_text="How thick is the tissue slice? Leave blank if culture."
    )
    slice_index = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="This is the order of the slice being cut from the block. The first slice cut is has an index of 1. Leave blank if culture.",
    )
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
    slide = models.ForeignKey(Slide, on_delete=models.SET_NULL, null=True, unique=False, default=None)

    # use "name" as alternative to "sample_id". this allows us to use our default foreign key display function in the admin panel
    @property
    def name(self):
        return self.sample_id

    class Meta:
        verbose_name_plural = "sample"

    def __str__(self):
        return "{}".format(self.sample_id)


class ExposureTime(models.Model):
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE)
    microscope = models.ForeignKey(Microscope, on_delete=models.CASCADE)
    exposure_time = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return "{} / {} / {} msec".format(self.probe, self.microscope, self.exposure_time)


class ProbeDilutions(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    probe = models.ForeignKey(Probe, on_delete=models.CASCADE)
    dilution = models.CharField(
        max_length=30,
        blank=True,
        default="",
        help_text="Dilutions should be represented as the ratio of the dilution factor from stock. So if working concentration is 1/100 of the stock concentration, then enter '1:100'",
    )

    def __str__(self):
        return "{} / {} / {}".format(self.panel, self.probe, self.dilution)

    class Meta:
        verbose_name_plural = "probe dilutions"
