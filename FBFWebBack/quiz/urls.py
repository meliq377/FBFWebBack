from django.urls import path
from .views import LessonListView, LessonDetailView, ModuleListView, SlideListView

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:lesson_id>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('modules/', ModuleListView.as_view(), name='module-list'),
    path('slides/', SlideListView.as_view(), name='slide-list'),
]