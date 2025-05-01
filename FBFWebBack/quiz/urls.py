from django.urls import path
from .views import LessonListView, LessonDetailView, LessonModuleListView, SlideListView

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:lesson_id>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('slides/', SlideListView.as_view(), name='slide-list'),
    path("lessons/<int:lesson_id>/modules/", LessonModuleListView.as_view(), name="lesson-modules"),
]