from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportModelAdmin
from import_export import resources
from .models import Question

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource
    list_display = ("text", "correct_option", "difficulty")
    search_fields = ("text",) 
    list_filter = ("difficulty",)  