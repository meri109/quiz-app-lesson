from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .models import Option, Question, QuizResult
from .serializers import QuestionSerializer, OptionSerializer, QuizResultSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from time import sleep


# Create your views here.


class QuestionListAV(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # def list(self, request, *args, **kwargs):
    #     sleep(4)
    #     return super().list(request, *args, **kwargs)

    
class QuestionDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer     

 
class QuizResultListAV(generics.ListCreateAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer

    
class QuizResultDetailAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizResult.objects.all()
    serializer_class = QuizResultSerializer 


   

