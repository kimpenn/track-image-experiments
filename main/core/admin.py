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
    Source,
    Slide,
    SliceOrCulture,
    Assay,
)


class ExposureTimeInLine(admin.TabularInline):
    model = ExposureTime
    extra = 0  # number of rows to show


class PanelProbesInLine(admin.TabularInline):
    model = Panel.probe.through
    extra = 0
    verbose_name_plural = "Probes used in panel"
    verbose_name = "probe"


class ProbePanelsInLine(admin.TabularInline):
    model = Panel.probe.through
    extra = 0
    verbose_name_plural = "Panel containing probe"
    verbose_name = "panel"


class AssayPanelsInLine(admin.TabularInline):
    model = Assay.panel.through
    extra = 0
    verbose_name_plural = "Panels used in assay"
    verbose_name = "panel"


class PanelAssaysInLine(admin.TabularInline):
    model = Assay.panel.through
    extra = 0
    verbose_name_plural = "Assays using panel"
    verbose_name = "assay"


class AssaySlidesInLine(admin.TabularInline):
    model = Assay.slide.through
    extra = 0
    verbose_name_plural = "Applied to these slides"
    verbose_name = "slide"


class SlideAssaysInLine(admin.TabularInline):
    model = Assay.slide.through
    extra = 0
    verbose_name_plural = "These assays used"
    verbose_name = "assay"


class SliceOrCultureInLine(admin.StackedInline):
    model = SliceOrCulture
    extra = 0
    verbose_name = "Sample"
    verbose_name_plural = "Samples"
    # fields = ["type", "parent", "organ", "organ_region", "treatment"]
    fieldsets = [
        ("Type", {"fields": ["type"]}),
        ("Origin", {"fields": ["parent", "organ", "organ_region"]}),
        (
            "Source",
            {
                "fields": [
                    "treatment",
                    "storage_time",
                    "prep_by",
                    "prep_date",
                    "acquired_from",
                ],
            },
        ),
        ("Slide", {"fields": ["slide"]}),
    ]


class CoreModelAdmin(admin.ModelAdmin):
    """
    This abstract model adds
        1. exporting of tables
        2. custom CSS for formatting of tabular inlines to remove "object" titles
    """

    class Meta:
        abstract = True

    # overwrite admin CSS
    class Media:
        css = {"all": ("css/core/custom_admin.css",)}

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

    """
    # remove the ability to bulk delete from the listview page
    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions
    """


class MicroscopeAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "model", "json_description"]


class ProbeResource(resources.ModelResource):
    probe_panel = fields.Field(
        column_name="probe_panel",
        attribute="probe_panel",
        widget=widgets.ManyToManyWidget(Panel, field="name", separator="|"),
    )

    class Meta:
        model = Probe


class ProbeAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "target_analyte", "probe_type", "fluorescent_molecule"]
    list_filter = ("target_analyte", "probe_type", "fluorescent_molecule")
    search_fields = ["name"]
    inlines = (
        ProbePanelsInLine,
        ExposureTimeInLine,
    )
    resource_classes = [ProbeResource]


class PanelAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "description"]
    exclude = ("probe",)
    inlines = (
        PanelProbesInLine,
        PanelAssaysInLine,
    )


class SourceAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "species", "sex", "age"]


class SlideAdmin(CoreModelAdmin, ImportExportModelAdmin):
    search_fields = ["name"]
    inlines = (
        SliceOrCultureInLine,
        SlideAssaysInLine,
    )


"""
class SliceOrCultureAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "type", "parent", "organ", "treatment"]
    list_filter = ("type", "parent", "organ", "treatment")
    search_fields = ["name"]

    fieldsets = [
        ("Type", {"fields": ["type"]}),
        ("Origin", {"fields": ["name", "parent", "organ", "organ_region"]}),
        (
            "Source",
            {
                "fields": [
                    "treatment",
                    "storage_time",
                    "prep_by",
                    "prep_date",
                    "acquired_from",
                ],
            },
        ),
        ("Slide", {"fields": ["slide"]}),
    ]
"""


class AssayResource(resources.ModelResource):
    probe_panel = fields.Field(
        column_name="probe_panel",
        attribute="probe_panel",
        widget=widgets.ManyToManyWidget(Panel, field="name", separator="|"),
    )

    class Meta:
        model = Assay


class AssayAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["assay_id", "staining_protocol", "microscope"]
    list_filter = ("staining_protocol", "microscope")
    search_fields = ["assay_id"]
    fieldsets = [
        (
            "Name",
            {
                "fields": ["assay_id"],
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
        AssayPanelsInLine,
        AssaySlidesInLine,
    )
    resource_classes = [AssayResource]


# we can remove models from this list, if we don't want them to show in the admin index.
# we use get_app_list() below to stop them from being sorted and rather they are listed
# in the order they are added with admin.site.register().
my_models = [
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
admin.site.register(Microscope, MicroscopeAdmin)
admin.site.register(Source, SourceAdmin)
# admin.site.register(SliceOrCulture, SliceOrCultureAdmin)
# admin.site.register(ExposureTime, ExposureTimeAdmin)
# admin.site.register(my_models, ImportExportModelAdmin)


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
