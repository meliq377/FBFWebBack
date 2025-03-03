from rest_framework import serializers
from .models import Lesson, Module, Slide, Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class SlideSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(source='quiz_set', many=True)  # Retrieve all quizzes related to a slide

    class Meta:
        model = Slide
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    slides = SlideSerializer(source='slide_set', many=True)  # Retrieve all slides related to a module

    class Meta:
        model = Module
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(source='module_set', many=True)  # Retrieve all modules related to a lesson

    class Meta:
        model = Lesson
        fields = '__all__'
