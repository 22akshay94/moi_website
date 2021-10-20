from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('home/education_list', EducationList.as_view()), # list of education items
    path('home/education_list/<int:pk>', EducationDetail.as_view()), # particular education item

    path('home/work_list', WorkList.as_view()), # list of work items
    path('home/work_list/<int:pk>', WorkDetail.as_view()), # particular work item

    path('home/project_list', ProjectList.as_view()), # list of project items
    path('home/project_list/<int:pk>', ProjectDetail.as_view()), # particular project item

    path('home/personal/<int:pk>', PersonalView.as_view()), # particular personal item
]