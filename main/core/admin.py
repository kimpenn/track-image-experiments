from django.contrib import admin

# Register your models here.
from .models import (
    Microscope,
    Donor,
    Panel,
    Probe,
    ExposureTime,
    ProbeTypes,
    FishTechnologies,
    FlourescentMolecules,
    ProbePanelIDs,
    ImagingSuccessOptions,
)

my_models = [
    Microscope,
    Donor,
    Panel,
    Probe,
    ExposureTime,
    ProbeTypes,
    FishTechnologies,
    FlourescentMolecules,
    ProbePanelIDs,
    ImagingSuccessOptions,
]
admin.site.register(my_models)
