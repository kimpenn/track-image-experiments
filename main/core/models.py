from django.db import models


# Create your models here.
class Microscope(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    json_description = models.FileField(upload_to="hardware_json/")


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
    age = models.PositiveSmallIntegerField()
