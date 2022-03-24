from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('categories/', views.ListCategoryAPI.as_view(), name='category-list'),
    path('doctors/', views.ListDoctorsAPI.as_view(), name='doctors-list'),
    path('doctors/<int:pk>/',
         views.RetrieveDoctorAPI.as_view(), name='doctor-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
