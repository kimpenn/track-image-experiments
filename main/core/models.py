import json
from django.db import models
from django.core.cache import cache

# Create your models here.


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
    sales_department = models.EmailField(blank=True)
    twilio_account_sid = models.CharField(
        max_length=255, default="ACbcad883c9c3e9d9913a715557dddff99"
    )
    twilio_auth_token = models.CharField(
        max_length=255, default="abd4d45dd57dd79b86dd51df2e2a6cd5"
    )
    twilio_phone_number = models.CharField(max_length=255, default="+15006660005")


def get_probe_types():
    all_settings = SiteSettings.objects.all()
    # create a list from the string field and then strip each element to remove extraneous spaces
    probe_type_list = [x.strip() for x in all_settings[0].probe_types.split(",")]
    # we actually need a list of tuples
    return list(zip(probe_type_list, probe_type_list))


class Probe(models.Model):
    id = models.CharField(primary_key=True, max_length=30, unique=True)
    target_analyte = models.CharField(max_length=255)
    target_gencode_id = models.CharField(max_length=255, blank=True, default="")
    probe_type = models.CharField(max_length=30, choices=get_probe_types(), null=True)
    antibody_clone_id = models.CharField(max_length=30, blank=True, default="")
    # fish_technology = models.CharField(max_length=30, choices=get_fish_technologies(), null=True)
    # fluorescent_molecule = models.CharField(max_length=30, choices=get_flourescent_molecules(), null=True)
    stock_concentration = models.CharField(max_length=30, blank=True, default="")
    working_dilution = models.CharField(max_length=30, blank=True, default="")
    # panel_id = models.CharField(max_length=30, choices=get_panel_ids(), null=True)
    # imaging_success = models.CharField(max_length=30, choices=get_imaging_success_options(), null=True)
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
