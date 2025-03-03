from .models import Question, GameSession
from rest_framework.serializers import ModelSerializer


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

class GameSessionSerializer(ModelSerializer):
    class Meta:
        model = GameSession
        fields = "__all__"
        read_only_fields = ["user", "is_active"]  # Այս դաշտերը swagger-ում editable չլինեն