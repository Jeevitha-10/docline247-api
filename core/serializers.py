from rest_framework import serializers
from .models import Category, Doctor


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon']


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'gender', 'category',
                  'age', 'year_of_employment', 'profile_pic']
