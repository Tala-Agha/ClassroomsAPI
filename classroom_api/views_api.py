from django.shortcuts import render
from classes.models import Classroom

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView
from .serializer import RegisterSerializer,ClassroomSerializer,ClassroomDetailSerializer,ClassroomCreateSerializer

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class ClassroomList(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class ClassroomDetail(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
    serializer_class = ClassroomCreateSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)

class ClassroomUpdate(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class ClassroomDelete(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
