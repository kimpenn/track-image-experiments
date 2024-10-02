from django.contrib import admin

# Register your models here.
from core.models import Microscope, Donor

my_models = [Microscope, Donor]
admin.site.register(my_models)
