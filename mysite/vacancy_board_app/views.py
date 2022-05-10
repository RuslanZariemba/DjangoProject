from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, template_name='vacancy_board_app/index.html')


def vacancies(request):
    return render(request, template_name='vacancy_board_app/vacancies.html')

def vacancy(request):
    return render(request, template_name='vacancy_board_app/vacancy.html')


def vacancies_by_specialty(request):
    return render(request, template_name='vacancy_board_app/vacancies.html')

def company(request):
    return render(request, template_name='vacancy_board_app/company.html')