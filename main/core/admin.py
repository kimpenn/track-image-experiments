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
    Sample,
    Assay,
    Vendor,
    Image,
)


class ExposureTimeInLine(admin.TabularInline):
    model = ExposureTime
    extra = 0  # number of rows to show


class PanelProbesInLine(admin.TabularInline):
    model = Panel.probe.through
    extra = 0
    verbose_name_plural = "Panel contains these probes"
    verbose_name = "probe"


class ProbePanelsInLine(admin.TabularInline):
    model = Panel.probe.through
    extra = 0
    verbose_name_plural = "Probe used in these panels"
    verbose_name = "panel"


class AssayPanelsInLine(admin.TabularInline):
    model = Assay.panel.through
    extra = 0
    verbose_name_plural = "Assay uses these panels"
    verbose_name = "panel"


class PanelAssaysInLine(admin.TabularInline):
    model = Assay.panel.through
    extra = 0
    verbose_name_plural = "Panel used in these assays"
    verbose_name = "assay"


class ImageSlideInLine(admin.StackedInline):
    model = Slide
    extra = 0
    verbose_name_plural = "Slide imaged"
    verbose_name = "slide"


"""
class AssaySlidesInLine(admin.TabularInline):
    model = Assay.slide.through
    extra = 0
    verbose_name_plural = "Assay applied to these slides"
    verbose_name = "slide"
"""

"""
class SlideAssaysInLine(admin.TabularInline):
    model = Assay.slide.through
    extra = 0
    verbose_name_plural = "Slide used with these assays"
    verbose_name = "assay"
"""


class DonorSamplesInLine(admin.TabularInline):
    model = Sample
    extra = 0
    verbose_name_plural = "Samples from this donor"
    verbose_name = "Sample"
    # fields = ["name",]


class SampleInLine(admin.StackedInline):
    model = Sample
    extra = 0
    verbose_name_plural = "Slide contains these samples"
    verbose_name = "Sample"
    # fields = ["type", "donor", "organ", "organ_region", "treatment"]
    fieldsets = [
        ("", {"fields": ["name", "type"]}),
        (
            "Origin",
            {
                "fields": ["donor", "organ", "organ_region"],
                "classes": ("expanded",),
            },
        ),
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
                "classes": ("expanded",),
            },
        ),
        # ("Slide", {"fields": ["slide"]}),
    ]


class CoreModelAdmin(admin.ModelAdmin):
    """
    This abstract model adds
        1. exporting of tables
        2. custom CSS for formatting of tabular inlines to remove "object" titles
    """

    class Meta:
        abstract = True

    # overwrite admin CSS to sort out extranious inline titles
    class Media:
        css = {"all": ("core/css/custom_admin.css",)}

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
    probe_type = fields.Field(
        column_name="probe_type",
        attribute="probe_type",
        widget=widgets.ForeignKeyWidget(ProbeTypes, field="name"),
    )
    fish_technology = fields.Field(
        column_name="fish_technology",
        attribute="fish_technology",
        widget=widgets.ForeignKeyWidget(FishTechnologies, field="name"),
    )
    fluorescent_molecule = fields.Field(
        column_name="fluorescent_molecule",
        attribute="fluorescent_molecule",
        widget=widgets.ForeignKeyWidget(FlourescentMolecules, field="name"),
    )
    vendor = fields.Field(
        column_name="vendor",
        attribute="vendor",
        widget=widgets.ForeignKeyWidget(Vendor, field="name"),
    )
    imaging_success = fields.Field(
        column_name="imaging_success",
        attribute="imaging_success",
        widget=widgets.ForeignKeyWidget(ImagingSuccessOptions, field="name"),
    )
    """
    # it seems the M2M only work in the model that contains the declaration (i.e., this works in the Panel model)
    panels = fields.Field(
        column_name="panels",
        attribute="panels",
        widget=widgets.ManyToManyWidget(Panel, field="name", separator="|"),
    )
    """

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


class PanelResource(resources.ModelResource):
    probe = fields.Field(
        column_name="probe",
        attribute="probe",
        widget=widgets.ManyToManyWidget(Probe, field="name", separator="|"),
    )

    class Meta:
        model = Panel


class PanelAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "description"]
    exclude = ("probe",)
    inlines = (
        PanelProbesInLine,
        PanelAssaysInLine,
    )
    resource_classes = [PanelResource]


class DonorResource(resources.ModelResource):
    species = fields.Field(
        column_name="species",
        attribute="species",
        widget=widgets.ForeignKeyWidget(Species, field="name"),
    )

    class Meta:
        model = Donor


class DonorAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "species", "sex", "age"]
    resource_classes = [DonorResource]
    inlines = (DonorSamplesInLine,)


class SlideAdmin(CoreModelAdmin, ImportExportModelAdmin):
    search_fields = ["slide_id"]
    list_display = ["slide_id"]
    inlines = (SampleInLine,)


class SampleAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "type", "donor", "organ", "treatment"]
    list_filter = ("type", "donor", "organ", "treatment")
    search_fields = ["name"]

    fieldsets = [
        ("Type", {"fields": ["type"]}),
        ("Origin", {"fields": ["name", "donor", "organ", "organ_region", "thickness", "slice_index"]}),
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


class AssayResource(resources.ModelResource):
    staining_protocol = fields.Field(
        column_name="staining_protocol",
        attribute="staining_protocol",
        widget=widgets.ForeignKeyWidget(StainingProtocols, field="name"),
    )
    staining_by = fields.Field(
        column_name="staining_by",
        attribute="staining_by",
        widget=widgets.ForeignKeyWidget(People, field="name"),
    )
    imaging_by = fields.Field(
        column_name="imaging_by",
        attribute="imaging_by",
        widget=widgets.ForeignKeyWidget(People, field="name"),
    )
    microscope = fields.Field(
        column_name="microscope",
        attribute="microscope",
        widget=widgets.ForeignKeyWidget(Microscope, field="name"),
    )
    panel = fields.Field(
        column_name="panel",
        attribute="panel",
        widget=widgets.ManyToManyWidget(Panel, field="name", separator="|"),
    )
    """
    slide = fields.Field(
        column_name="slide",
        attribute="slide",
        widget=widgets.ManyToManyWidget(Slide, field="name", separator="|"),
    )
    """

    class Meta:
        model = Assay


class ImageAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["image_id", "assay", "slide"]
    list_filter = ("staining_by", "imaging_by", "microscope")
    search_fields = ["image_id"]
    fieldsets = [
        (
            "",
            {
                "fields": ["image_id", "assay", "slide"],
            },
        ),
        (
            "Staining",
            {
                "fields": ["staining_by", "staining_date"],
            },
        ),
        (
            "Imaging",
            {
                "fields": ["microscope", "imaging_by", "imaging_date"],
            },
        ),
    ]
    # inlines = (ImageSlideInLine,)
    # resource_classes = [ImageResource]


class AssayAdmin(CoreModelAdmin, ImportExportModelAdmin):
    list_display = ["name", "staining_protocol"]
    list_filter = ("staining_protocol",)
    search_fields = ["name"]
    exclude = ("panel",)
    """
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
                "fields": ["staining_protocol"],
            },
        ),
    ]
    """
    inlines = (
        AssayPanelsInLine,
        # AssaySlidesInLine,
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
    Vendor,
]
admin.site.register(Image, ImageAdmin)
admin.site.register(Assay, AssayAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Panel, PanelAdmin)
admin.site.register(Probe, ProbeAdmin)
admin.site.register(Microscope, MicroscopeAdmin)
admin.site.register(Donor, DonorAdmin)

admin.site.register(Sample, SampleAdmin)
admin.site.register(ExposureTime)
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
