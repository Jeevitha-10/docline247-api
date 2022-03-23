from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('doctors/', views.DoctorList.as_view(), name='doctors-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
