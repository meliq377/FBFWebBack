from djoser.serializers import UserCreateSerializer
from accounts.models import CustomUser


class UserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "first_name", "last_name", "password")
