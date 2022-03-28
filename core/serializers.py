from rest_framework import serializers
from .models import Appointment, Category, Doctor, Patient


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'icon']


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'gender', 'category',
                  'age', 'year_of_employment', 'profile_pic']


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'name', 'email', 'dob']


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'date_of_appointment', 'category',
                  'doctor', 'time_slot', 'message', 'slug', 'status']
