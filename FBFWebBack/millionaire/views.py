import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question

class QuestionListView(APIView):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.all()
        response_data = []

        for question in questions:
            difficulty = question.difficulty
            correct_option = question.correct_option
            
            # Define probability distribution based on difficulty
            if difficulty == 1:  # Easy
                correct_percentage = 80
            elif difficulty == 2:  # Medium
                correct_percentage = 60
            else:  # Hard
                correct_percentage = 40

            # Remaining percentage for incorrect answers
            remaining_percentage = 100 - correct_percentage
            
            # Generate three random weights that sum to remaining_percentage
            incorrect_percentages = sorted([random.uniform(0, remaining_percentage) for _ in range(2)])
            incorrect1 = round(incorrect_percentages[0], 2)
            incorrect2 = round(incorrect_percentages[1] - incorrect_percentages[0], 2)
            incorrect3 = round(remaining_percentage - incorrect_percentages[1], 2)

            # Assign percentages to options
            options = {
                question.option1: incorrect1 if correct_option != 1 else correct_percentage,
                question.option2: incorrect2 if correct_option != 2 else correct_percentage,
                question.option3: incorrect3 if correct_option != 3 else correct_percentage,
                question.option4: round(remaining_percentage - (incorrect1 + incorrect2 + incorrect3), 2) if correct_option != 4 else correct_percentage,
            }

            question_data = {
                "id": question.id,
                "text": question.text,
                "options": options,
                "correct_option": correct_option,
                "call_answer": getattr(question, f"option{correct_option}"),
            }
            response_data.append(question_data)

        return Response(response_data, status=status.HTTP_200_OK)
