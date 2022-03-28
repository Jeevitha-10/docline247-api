from rest_framework import generics
from .models import Appointment, Category, Doctor, Patient
from .serializers import AppointmentSerializer, CategorySerializer, DoctorSerializer, PatientSerializer
from .pagination import DoctorsListPagination


class ListCategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListDoctorsAPI(generics.ListAPIView):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    pagination_class = DoctorsListPagination


class RetrieveDoctorAPI(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class ListPatientsAPI(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class ListAppointmentsAPI(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class RetrieveAppointmentAPI(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
