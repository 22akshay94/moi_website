from rest_framework import generics
from .models import Project, Education, Work, Personal
from .serializers import *

class EducationList(generics.ListCreateAPIView):
    queryset = Education.item_objs.all()
    serializer_class = EducationSerializer

class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.item_objs.all()
    serializer_class = EducationSerializer



class WorkList(generics.ListCreateAPIView):
    queryset = Work.item_objs.all()
    serializer_class = WorkSerializer

class WorkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.item_objs.all()
    serializer_class = WorkSerializer



class ProjectList(generics.ListCreateAPIView):
    queryset = Project.project_objs.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.project_objs.all()
    serializer_class = ProjectSerializer



class PersonalView(generics.ListCreateAPIView):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer