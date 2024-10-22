import json
from django.db import models
from django.core.cache import cache

# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Organs(models.Model):
    name = models.CharField(max_length=30, unique=True)


class OrganRegions(models.Model):
    name = models.CharField(max_length=30, unique=True)


class ProbeTypes(models.Model):
    name = models.CharField(max_length=30, unique=True)


class FishTechnologies(models.Model):
    name = models.CharField(max_length=30, unique=True)


class FlourescentMolecules(models.Model):
    name = models.CharField(max_length=30, unique=True)


class ProbePanels(models.Model):
    name = models.CharField(max_length=30, unique=True)


class ImagingSuccessOptions(models.Model):
    name = models.CharField(max_length=30, unique=True)


# not sure how to keep this from accessing the database when module is first imported
def get_choices(model):
    rows = model.objects.all()
    options = [row.name.strip() for row in rows]
    return list(zip(options, options))


class Probe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    target_analyte = models.CharField(max_length=255)
    target_gencode_id = models.CharField(max_length=255, blank=True, default="")
    probe_type = models.ForeignKey(ProbeTypes, on_delete=models.SET_NULL, null=True)
    antibody_clone_id = models.CharField(max_length=30, blank=True, default="")
    fish_technology = models.ForeignKey(FishTechnologies, on_delete=models.SET_NULL, null=True)
    fluorescent_molecule = models.ForeignKey(FlourescentMolecules, on_delete=models.SET_NULL, null=True)
    stock_concentration = models.CharField(max_length=30, blank=True, default="")
    working_dilution = models.CharField(max_length=30, blank=True, default="")
    probe_panel = models.ForeignKey(ProbePanels, on_delete=models.SET_NULL, null=True)
    imaging_success = models.ForeignKey(ImagingSuccessOptions, on_delete=models.SET_NULL, null=True)
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


class Slides(models.Model):
    name = models.CharField(max_length=30, unique=True, default="")
    # species = models.CharField(max_length=30, choices=get_choices(Species), null=True)
    # organ = models.CharField(max_length=30, choices=get_choices(Organs), null=True)
    # organ_region = models.CharField(max_length=30, choices=get_choices(OrganRegions), null=True)
