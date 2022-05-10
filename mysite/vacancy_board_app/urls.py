from django.urls import path
from .views import company, index, vacancies, vacancies_by_specialty

urlpatterns = [
    path('', index, name='index'),
    path('vacancies/', vacancies, name='vacancies'),
    path('vacancies/1', vacancies, name='vacancies'),
    path('vacancies/cat/frontend', vacancies_by_specialty, name='vacancies'),
    path('companies/1', company, name='company'),
]
