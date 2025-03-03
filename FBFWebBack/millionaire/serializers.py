from .models import Question, GameSession
from rest_framework.serializers import ModelSerializer


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "all"

class GameSessionSerializer(ModelSerializer):
    class Meta:
        model = GameSession
        fields = "all"
        read_only_fields = ["user", "is_active"]  # Այս դաշտերը swagger-ում editable չլինեն