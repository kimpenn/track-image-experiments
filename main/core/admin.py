from django.contrib import admin

# from .forms import GetForeignKeyName, GetManyToManyName


# Register your models here.
from .models import (
    Species,
    Organs,
    OrganRegions,
    MaterialSources,
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


class ProbeAdmin(admin.ModelAdmin):
    list_display = ["name", "target_analyte", "probe_type", "fluorescent_molecule"]


class PanelAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "probe_list"]


class ExposureTimeAdmin(admin.ModelAdmin):
    list_display = ["probe", "microscope", "exposure_time"]


class SlidesAdmin(admin.ModelAdmin):
    list_display = ["name", "species", "organ", "staining_protocol"]

    fieldsets = [
        ("Origin", {"fields": ["name", "species", "organ", "organ_region", "donor"]}),
        (
            "Source",
            {
                "fields": ["material_source", "source_format", "source_prep_by", "source_prep_date"],
            },
        ),
        (
            "Staining",
            {
                "fields": ["probe_panel", "staining_protocol", "staining_by", "staining_date"],
            },
        ),
        (
            "Imaging",
            {
                "fields": ["microscope", "imaging_by", "imaging_date"],
            },
        ),
    ]


# we can remove models from this list, if we don't want them to show in the admin index.
# we use get_app_list() below to stop them from being sorted and rather they are listed
# in the order they are added with admin.site.register().
my_models = [
    Donor,
    Microscope,
    FishTechnologies,
    FlourescentMolecules,
    ImagingSuccessOptions,
    MaterialSources,
    Organs,
    OrganRegions,
    People,
    ProbePanels,
    ProbeTypes,
    Species,
    StainingProtocols,
]
admin.site.register(Slides, SlidesAdmin)
admin.site.register(Panel, PanelAdmin)
admin.site.register(Probe, ProbeAdmin)
admin.site.register(ExposureTime, ExposureTimeAdmin)
admin.site.register(my_models)


def get_app_list(self, request, app_label=None):
    """Return the installed apps that have been registered in admin.py.
    https://forum.djangoproject.com/t/reordering-list-of-models-in-django-admin/5300/9"""
    app_dict = self._build_app_dict(request, app_label)
    app_list = list(app_dict.values())
    # Do not sort models alphatbetically
    # for app in app_list:
    #    app["models"].sort(key=lambda x: x["name"])
    return app_list


admin.AdminSite.get_app_list = get_app_list
