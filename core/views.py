from rest_framework import generics
from .models import Category, Doctor
from .serializers import CategorySerializer, DoctorSerializer
from .pagination import DoctorsListPagination


class ListCategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListDoctorsAPI(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorsListPagination


class RetrieveDoctorAPI(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
