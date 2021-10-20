from operator import itemgetter
from collections import OrderedDict
from rest_framework import serializers
from .models import Project, Education, Work, Personal

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret

class EducationSerializer(serializers.ModelSerializer):

    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):

    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Work
        fields = '__all__'

class PersonalSerializer(serializers.ModelSerializer):\

    education = EducationSerializer(many=True, read_only=True)
    work = WorkSerializer(many=True, read_only=True)

    class Meta:
        model = Personal
        fields = '__all__'