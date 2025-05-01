from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Lesson, Module, Slide
from .serializers import LessonSerializer, ModuleSerializer, SlideSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import TokenAuthentication


class LessonListView(APIView):
    """
    Retrieve all lessons with their related modules, slides, and quizzes.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        print("----- DEBUG -----")
        print("AUTH HEADER :", request.META.get("HTTP_AUTHORIZATION"))
        print("REQUEST.USER:", request.user)
        print("-----------------")
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
class LessonDetailView(APIView):
    """
    Retrieve a single lesson by its ID, including its related modules, slides, and quizzes.
    """
    def get(self, request, lesson_id, *args, **kwargs):
        try:
            lesson = Lesson.objects.get(id=lesson_id)
            serializer = LessonSerializer(lesson)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Lesson.DoesNotExist:
            return Response({"error": "Lesson not found"}, status=status.HTTP_404_NOT_FOUND)


class LessonModuleListView(APIView):
    """
    Retrieve all modules for a specific lesson (with slides and quizzes).
    """

    def get(self, request, lesson_id, *args, **kwargs):
        modules = Module.objects.filter(lesson_id=lesson_id)
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SlideListView(APIView):
    """
    Retrieve all slides with their related quizzes.
    """
    def get(self, request, *args, **kwargs):
        slides = Slide.objects.all()
        serializer = SlideSerializer(slides, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)