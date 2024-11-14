import csv
from django.contrib import admin
from django.forms import Field
from django.http import HttpResponse
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields, widgets


# Register your models here.
from .models import (
    Species,
    Organs,
    OrganRegions,
    MaterialSources,
    SourceTreatments,
    People,
    StainingProtocols,
    ProbeTypes,
    FishTechnologies,
    FlourescentMolecules,
    ImagingSuccessOptions,
    Probe,
    Panel,
    Microscope,
    ExposureTime,
    Donor,
    Slide,
    Assay,
)


class ExposureTimeInLine(admin.TabularInline):
    model = ExposureTime
    extra = 0  # number of rows to show


class ProbeInLine(admin.TabularInline):
    model = Probe.probe_panel.through
    extra = 0
    # verbose_name = "Panel"
    # verbose_name_plural = "Panels"


class AssayInLine(admin.TabularInline):
    model = Assay.probe_panel.through
    extra = 0


class SlideInLine(admin.TabularInline):
    model = Slide.assay.through
    extra = 0


class ModelAdminWithExport(admin.ModelAdmin):  # Abstract model, assuming a name field
    class Meta:
        abstract = True

    """
    # remove the ability to bulk delete from the listview page
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions
    """

    # add exporting option to listview page
    actions = ("export_to_csv",)

    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment; filename={}.csv".format(meta.verbose_name_plural)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_to_csv.short_description = "Export Selected"


class ExposureTimeAdmin(ModelAdminWithExport, ImportExportModelAdmin):
    list_display = ["probe", "microscope", "exposure_time"]


class MicroscopeAdmin(ModelAdminWithExport, ImportExportModelAdmin):
    list_display = ["name", "model", "json_description"]


class ProbeResource(resources.ModelResource):
    probe_panel = fields.Field(
        column_name="probe_panel",
        attribute="probe_panel",
        widget=widgets.ManyToManyWidget(Panel, field="name", separator="|"),
    )

    class Meta:
        model = Probe


class ProbeAdmin(ModelAdminWithExport, ImportExportModelAdmin):
    list_display = ["name", "target_analyte", "probe_type", "fluorescent_molecule"]
    # inlines = [ExposureTimeInLine]
    list_filter = ("target_analyte", "probe_type", "fluorescent_molecule")
    search_fields = ["name"]
    exclude = ("probe_panel",)
    inlines = (
        ProbeInLine,
        ExposureTimeInLine,
    )
    resource_classes = [ProbeResource]


class PanelAdmin(ModelAdminWithExport, ImportExportModelAdmin):
    list_display = ["name", "description"]
    inlines = (
        ProbeInLine,
        AssayInLine,
    )


class SlideAdmin(ModelAdminWithExport, ImportExportModelAdmin):
    list_display = ["name", "species", "organ", "donor"]
    list_filter = ("species", "organ", "source_format")
    search_fields = ["name"]

    fieldsets = [
        ("Origin", {"fields": ["name", "species", "organ", "organ_region", "donor"]}),
        (
            "Source",
            {
                "fields": [
                    "material_source",
                    "source_treatment",
                    "source_storage_time",
                    "source_format",
                    "source_prep_by",
                    "source_prep_date",
                ],
            },
        ),
    ]
    inlines = (SlideInLine,)


class AssayResource(resources.ModelResource):
    probe_panel = fields.Field(
        column_name="probe_panel",
        attribute="probe_panel",
        widget=widgets.ManyToManyWidget(Panel, field="name", separator="|"),
    )

    class Meta:
        model = Assay


class AssayAdmin(ModelAdminWithExport, ImportExportModelAdmin):
    list_display = ["name", "staining_protocol", "microscope"]
    list_filter = ("staining_protocol", "microscope")
    search_fields = ["name"]
    fieldsets = [
        (
            "Name",
            {
                "fields": ["name"],
            },
        ),
        (
            "Staining",
            {
                "fields": ["staining_protocol", "staining_by", "staining_date"],
            },
        ),
        (
            "Imaging",
            {
                "fields": ["microscope", "imaging_by", "imaging_date"],
            },
        ),
    ]
    inlines = (
        AssayInLine,
        SlideInLine,
    )
    resource_classes = [AssayResource]


# we can remove models from this list, if we don't want them to show in the admin index.
# we use get_app_list() below to stop them from being sorted and rather they are listed
# in the order they are added with admin.site.register().
my_models = [
    Donor,
    FishTechnologies,
    FlourescentMolecules,
    ImagingSuccessOptions,
    MaterialSources,
    SourceTreatments,
    Organs,
    OrganRegions,
    People,
    ProbeTypes,
    Species,
    StainingProtocols,
]
admin.site.register(Assay, AssayAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Panel, PanelAdmin)
admin.site.register(Probe, ProbeAdmin)
admin.site.register(ExposureTime, ExposureTimeAdmin)
admin.site.register(Microscope, MicroscopeAdmin)
admin.site.register(my_models, ImportExportModelAdmin)


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
