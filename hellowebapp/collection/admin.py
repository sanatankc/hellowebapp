from django.contrib import admin
from .models import Thing

# set up automated slugcreation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.
admin.site.register(Thing, ThingAdmin)