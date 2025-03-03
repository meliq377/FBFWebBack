from django.contrib import admin
from import_export.admin import ExportMixin
from import_export import resources
from .models import Lesson, Module, Slide, Quiz

# Define resource classes for import/export
class LessonResource(resources.ModelResource):
    class Meta:
        model = Lesson

class ModuleResource(resources.ModelResource):
    class Meta:
        model = Module

class SlideResource(resources.ModelResource):
    class Meta:
        model = Slide

class QuizResource(resources.ModelResource):
    class Meta:
        model = Quiz

# Register models with admin using Import-Export
@admin.register(Lesson)
class LessonAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LessonResource
    list_display = ('lesson_title', 'lesson_description')

@admin.register(Module)
class ModuleAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ModuleResource
    list_display = ('module_title', 'module_description', 'lesson')

@admin.register(Slide)
class SlideAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = SlideResource
    list_display = ('slide_title', 'module')

@admin.register(Quiz)
class QuizAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = QuizResource
    list_display = ('slide', 'question', 'correct_option')
