from django.urls import path
from .views import LessonListView

urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
]
