from django.urls import path
from .views import (
    StartGameAPIView,
    CurrentQuestionAPIView,
    SubmitAnswerAPIView,
    UseFiftyFiftyAPIView,
    UsePhoneFriendAPIView,
    UseAudienceHelpAPIView,
)

urlpatterns = [
    path("start/", StartGameAPIView.as_view(), name="start_game"),
    path("current/", CurrentQuestionAPIView.as_view(), name="current_question"),
    path("answer/", SubmitAnswerAPIView.as_view(), name="submit_answer"),
    path("lifeline/5050/", UseFiftyFiftyAPIView.as_view(), name="use_5050"),
    path("lifeline/phone/", UsePhoneFriendAPIView.as_view(), name="use_phone_friend"),
    path("lifeline/audience/", UseAudienceHelpAPIView.as_view(), name="use_audience_help"),
]