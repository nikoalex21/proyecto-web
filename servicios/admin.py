from django.contrib import admin
from servicios.models import Servicio

# Register your models here.
class servicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') #solo lectura

admin.site.register(Servicio, servicioAdmin)


