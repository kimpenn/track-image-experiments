from django.contrib import admin

from .forms import GetForeignKeyName, GetManyToManyName


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


my_models = [
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
    # Probe,
    # Panel,
    Microscope,
    # ExposureTime,
    Donor,
    # Slides,
]
admin.site.register(my_models)


class ProbeAdmin(admin.ModelAdmin):
    list_display = ["name", "target_analyte", "probe_type"]


admin.site.register(Probe, ProbeAdmin)


class PanelAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "probe_list"]


admin.site.register(Panel, PanelAdmin)


class ExposureTimeAdmin(admin.ModelAdmin):
    list_display = ["probe", "microscope", "exposure_time"]

    """
    # list_display = ["get_probe", "get_microscope", "exposure_time"]
    # this is a foreign key and we want the name field
    def get_probe(self, obj):
        return obj.probe.name
    get_probe.admin_order_field = "probe"  # Allows column order sorting
    get_probe.short_description = "Probes"  # Renames column head
    """

    """
    # this is not necessary where the model str() returns the name
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # if db_field.name = "probe" then this will return the Probe table
        model = ExposureTime._meta.get_field(db_field.name).related_model
        return GetForeignKeyName(queryset=model.objects.all())
        # This is another way to do it, if I want a different option per field/table
        # if db_field.name == "probe":
        #    return GetForeignKeyName(queryset=Probe.objects.all())
        # return super().formfield_for_foreignkey(db_field, request, **kwargs)
    """


admin.site.register(ExposureTime, ExposureTimeAdmin)


class SlidesAdmin(admin.ModelAdmin):
    list_display = ["name", "species", "organ"]

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

    """
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        model = Slides._meta.get_field(db_field.name).related_model
        return GetManyToManyName(queryset=model.objects.all())
    """


admin.site.register(Slides, SlidesAdmin)
