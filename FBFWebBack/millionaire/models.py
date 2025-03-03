# Create your models here.
from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    DIFFICULTY_CHOICES = (
        (1, "Easy"),
        (2, "Medium"),
        (3, "Hard"),
    )
    text = models.CharField(max_length=255)  
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField(help_text="1 to 4") 
    difficulty = models.PositiveSmallIntegerField(choices=DIFFICULTY_CHOICES)

    def str(self):
        return self.text


class GameSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    current_question_index = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=20)

    used_fifty_fifty = models.BooleanField(default=False)
    used_phone_friend = models.BooleanField(default=False)
    used_audience_help = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def str(self):
        return f"{self.user.username} - GameSession"