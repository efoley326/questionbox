from django.shortcuts import render
from rest_framework import generics
<<<<<<< HEAD
from .models import Question, Answer, Tag
=======
from .models import Question, Answer, Tag, User
from library.serializers import QuestionSerializer, AnswerSerializer, UserSerializer, TagSerializer
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import io
>>>>>>> d20a038a4656a16db39c196f63d86dd052e9b824
# from .serializers import 

# Create your views here.

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
<<<<<<< HEAD
=======
    serializer_class = QuestionSerializer
    permission_classes = [User]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = Question.Serializer(queryset, many=True)
        return Response(serializer.data)
>>>>>>> d20a038a4656a16db39c196f63d86dd052e9b824


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
<<<<<<< HEAD
=======

    def get_question(self, pk):
        return Question.objects.get(pk=pk)
>>>>>>> d20a038a4656a16db39c196f63d86dd052e9b824

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class =  AnswerSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()

    def get_answer(self, pk):
        return Answer.objects.get(pk=pk)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = AnswerSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            



class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TagSerializer(queryset, many=True)
        return Response(serializer.data)



class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def put(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)