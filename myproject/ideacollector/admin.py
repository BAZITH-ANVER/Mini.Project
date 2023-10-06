from django.contrib import admin

# Register your models here.
from.models import Student,Frontend,Backend,Framework,Course
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class Students(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=('Fullname','Mobile','Projectname','Desciption','Frontend','Backendend','Framework','Course')


admin.site.register(Student)
admin.site.register(Frontend)
admin.site.register(Backend)
admin.site.register(Framework)
admin.site.register(Course)
