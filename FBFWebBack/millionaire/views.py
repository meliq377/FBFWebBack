from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import GameSession, Question
from .serializers import GameSessionSerializer, QuestionSerializer
import random

class StartGameAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        GameSession.objects.filter(user=request.user, is_active=True).update(is_active=False)

        game_session = GameSession.objects.create(user=request.user)

        return Response(
            GameSessionSerializer(game_session).data,
            status=status.HTTP_201_CREATED
        )


class CurrentQuestionAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        game_session = get_object_or_404(GameSession, user=request.user, is_active=True)
        current_index = game_session.current_question_index

        if current_index < 7:
            questions = Question.objects.filter(difficulty=1)
        elif current_index < 14:
            questions = Question.objects.filter(difficulty=2)
        else:
            questions = Question.objects.filter(difficulty=3)

        question_list = questions.order_by("?")
       
        if not question_list.exists():
            return Response({"detail": "No questions found"}, status=status.HTTP_404_NOT_FOUND)

        question = question_list.first()
        
        return Response(
            QuestionSerializer(question).data,
            status=status.HTTP_200_OK
        )


class SubmitAnswerAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        game_session = get_object_or_404(GameSession, user=request.user, is_active=True)
        current_index = game_session.current_question_index

        if current_index < 7:
            questions = Question.objects.filter(difficulty=1)
        elif current_index < 14:
            questions = Question.objects.filter(difficulty=2)
        else:
            questions = Question.objects.filter(difficulty=3)

        question = questions.order_by("?").first()

        selected_option = request.data.get("selected_option")

        if question.correct_option == selected_option:
            game_session.current_question_index += 1

            if game_session.current_question_index >= game_session.total_questions:
                game_session.is_active = False

            game_session.save()
            return Response({"detail": "Correct answer!"}, status=status.HTTP_200_OK)

        else:
            game_session.is_active = False
            game_session.save()
            return Response({"detail": "Wrong answer! Game over."}, status=status.HTTP_200_OK)


class UseFiftyFiftyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        game_session = get_object_or_404(GameSession, user=request.user, is_active=True)
        if game_session.used_fifty_fifty:
            return Response({"detail": "You have already used 50-50"}, status=status.HTTP_400_BAD_REQUEST)
        
        game_session.used_fifty_fifty = True
        game_session.save()

        current_index = game_session.current_question_index
        if current_index < 7:
            questions = Question.objects.filter(difficulty=1)
        elif current_index < 14:
            questions = Question.objects.filter(difficulty=2)
        else:
            questions = Question.objects.filter(difficulty=3)
        question = questions.order_by("?").first()
        
        correct_opt = question.correct_option 
        all_options = [1, 2, 3, 4]
        all_options.remove(correct_opt)
        import random
        random_to_keep = random.choice(all_options)
        final_options = [correct_opt, random_to_keep]
        final_options.sort()
        
        return Response(
            {
                "question_id": question.id,
                "remaining_options": final_options
            },
            status=status.HTTP_200_OK
        )


class UsePhoneFriendAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        game_session = get_object_or_404(GameSession, user=request.user, is_active=True)
        if game_session.used_phone_friend:
            return Response({"detail": "You have already used Phone Friend"}, status=status.HTTP_400_BAD_REQUEST)

        game_session.used_phone_friend = True
        game_session.save()

        current_index = game_session.current_question_index
        if current_index < 7:
            questions = Question.objects.filter(difficulty=1)
            hint_correct_probability = 0.8
        elif current_index < 14:
            questions = Question.objects.filter(difficulty=2)
            hint_correct_probability = 0.6
        else:
            questions = Question.objects.filter(difficulty=3)
            hint_correct_probability = 0.4

        question = questions.order_by("?").first()

        import random
        is_hint_correct = random.random() < hint_correct_probability
        if is_hint_correct:
            phone_friend_suggestion = question.correct_option
        else:
            all_opts = [1,2,3,4]
            all_opts.remove(question.correct_option)
            phone_friend_suggestion = random.choice(all_opts)

        return Response(
            {
                "phone_friend_says": phone_friend_suggestion
            },
            status=status.HTTP_200_OK
        )


class UseAudienceHelpAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        game_session = get_object_or_404(GameSession, user=request.user, is_active=True)
        if game_session.used_audience_help:
            return Response({"detail": "You have already used Audience Help"}, status=status.HTTP_400_BAD_REQUEST)

        game_session.used_audience_help = True
        game_session.save()

        current_index = game_session.current_question_index
        if current_index < 7:
            questions = Question.objects.filter(difficulty=1)
            audience_correct_probability = 0.7
        elif current_index < 14:
            questions = Question.objects.filter(difficulty=2)
            audience_correct_probability = 0.5
        else:
            questions = Question.objects.filter(difficulty=3)
            audience_correct_probability = 0.3

        question = questions.order_by("?").first()

        import random
        is_hint_correct = random.random() < audience_correct_probability
        if is_hint_correct:
            audience_suggestion = question.correct_option
        else:
            all_opts = [1,2,3,4]
            all_opts.remove(question.correct_option)
            audience_suggestion = random.choice(all_opts)

        return Response(
            {
                "audience_says": audience_suggestion
            },
            status=status.HTTP_200_OK
        )