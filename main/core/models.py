import json
from django.db import models
from django.core.cache import cache

# Create your models here.

"""
# see https://globaldev.tech/blog/practical-application-singleton-design-pattern
class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class SiteSettings(SingletonModel):
    probe_types = models.TextField(blank=True)
    # fish_technologies = models.TextField(blank=True)
    # flourescent_molecules = models.TextField(blank=True)
    # panel_ids = models.TextField(blank=True)
    # imaging_success_options = models.TextField(blank=True)

 
def get_probe_types():
    all_settings = SiteSettings.objects.all()
    # create a list from the string field and then strip each element to remove extraneous spaces
    options_list = [x.strip() for x in all_settings[0].probe_types.split(",")]
    # we actually need a list of tuples
    return list(zip(options_list, options_list))

def get_probe_types():
    return get_choices(ProbeTypes)

def get_fish_technologies():
    rows = FishTechnologies.objects.all()
    values = [row.technology.strip() for row in rows]
    return list(zip(values, values))

"""


class ProbeTypes(models.Model):
    option = models.CharField(max_length=30, unique=True)


class FishTechnologies(models.Model):
    option = models.CharField(max_length=30, unique=True)


class FlourescentMolecules(models.Model):
    option = models.CharField(max_length=30, unique=True)


class ProbePanelIDs(models.Model):
    option = models.CharField(max_length=30, unique=True)


class ImagingSuccessOptions(models.Model):
    option = models.CharField(max_length=30, unique=True)


def get_choices(model):
    rows = model.objects.all()
    options = [row.option.strip() for row in rows]
    return list(zip(options, options))


class Probe(models.Model):
    id = models.CharField(primary_key=True, max_length=30, unique=True)
    target_analyte = models.CharField(max_length=255)
    target_gencode_id = models.CharField(max_length=255, blank=True, default="")
    probe_type = models.CharField(
        max_length=30, choices=get_choices(ProbeTypes), null=True
    )
    antibody_clone_id = models.CharField(max_length=30, blank=True, default="")
    fish_technology = models.CharField(
        max_length=30, choices=get_choices(FishTechnologies), null=True
    )
    fluorescent_molecule = models.CharField(
        max_length=30, choices=get_choices(FlourescentMolecules), null=True
    )
    stock_concentration = models.CharField(max_length=30, blank=True, default="")
    working_dilution = models.CharField(max_length=30, blank=True, default="")
    probe_panel_id = models.CharField(
        max_length=30, choices=get_choices(ProbePanelIDs), null=True
    )
    imaging_success = models.CharField(
        max_length=30, choices=get_choices(ImagingSuccessOptions), null=True
    )
    staining_notes = models.TextField(blank=True, default="")
    imaging_notes = models.TextField(blank=True, default="")
    # Akoya Fusion exposure time
    # Observer 7 exposure time


class Panel(models.Model):
    id = models.CharField(primary_key=True, max_length=30, unique=True)
    description = models.CharField(max_length=255, blank=True, default="")
    notes = models.TextField(blank=True, default="")
    probe_list = models.CharField(max_length=255, blank=True, default="")


class Microscope(models.Model):
    id = models.CharField(primary_key=True, max_length=30, unique=True)
    model = models.CharField(max_length=30)
    json_description = models.FileField(
        upload_to="hardware_json/", blank=True, null=True
    )


class ExposureTime(models.Model):
    probe_id = models.ForeignKey(Probe, on_delete=models.CASCADE)
    microscope_id = models.ForeignKey(Microscope, on_delete=models.CASCADE)
    exposure_time = models.DecimalField(decimal_places="4", max_digits=6)


class Donor(models.Model):
    FEMALE = "F"
    MALE = "M"
    UNKNOWN = "U"
    SEX = {
        FEMALE: "Female",
        MALE: "Male",
        UNKNOWN: "Unknown",
    }

    id = models.CharField(primary_key=True, max_length=30, unique=True)
    sex = models.CharField(max_length=1, choices=SEX, default=UNKNOWN)
    age = models.PositiveSmallIntegerField(blank=True)
