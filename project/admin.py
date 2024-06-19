from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin

# from import_export import resources
# from core.models import Book


# Register your models here.

# class BookResource(resources.ModelResource):

#     class Meta:
#         model = Book  # or 'core.Book'

# admin.site.register(Project)
@admin.register(Project)
class ProjectImportExport(ImportExportModelAdmin):
    pass

