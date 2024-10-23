from django.contrib import admin

from .forms import GetChoiceField


# Register your models here.
from .models import (
    Species,
    Organs,
    OrganRegions,
    People,
    StainingProtocols,
    ProbeTypes,
    FishTechnologies,
    FlourescentMolecules,
    ProbePanels,
    ImagingSuccessOptions,
    Probe,
    Panel,
    Microscope,
    ExposureTime,
    Donor,
    Slides,
)


my_models = [
    Species,
    Organs,
    OrganRegions,
    People,
    StainingProtocols,
    ProbeTypes,
    FishTechnologies,
    FlourescentMolecules,
    ProbePanels,
    ImagingSuccessOptions,
    # Probe,
    Panel,
    Microscope,
    # ExposureTime,
    Donor,
    Slides,
]
admin.site.register(my_models)


class ProbeAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        model = Probe._meta.get_field(db_field.name).related_model
        return GetChoiceField(queryset=model.objects.all())


class ExposureTimeAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # if db_field.name = "probe" then this will return the Probe table
        model = ExposureTime._meta.get_field(db_field.name).related_model
        return GetChoiceField(queryset=model.objects.all())
        # This is another way to do it, if I want a different option per field/table
        # if db_field.name == "probe":
        #    return GetChoiceField(queryset=Probe.objects.all())
        # return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Probe, ProbeAdmin)
admin.site.register(ExposureTime, ExposureTimeAdmin)
