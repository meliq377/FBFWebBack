from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lesson, Module, Slide, Quiz
from .serializers import LessonSerializer

class LessonListView(APIView):
    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
