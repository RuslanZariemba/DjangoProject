from django.core.management.base import BaseCommand
from django.db import models
from django.db.models import Model

from test_data import specialties, jobs, companies
from vacancy_board_app.models import Specialty, Company, Vacancy


class Command(BaseCommand):

    def handle(self, *args, **options):

        # Добавляет специализации из test_data.py
        all_specialty = Specialty.objects.all()
        new_specialties = []

        for spec in specialties:
            if all_specialty.filter(code=spec['code']).count() == 0:
                new_specialties.append(Specialty(code=spec['code'], title=spec['title']))
        if new_specialties:
            try:
                Specialty.objects.bulk_create(new_specialties)
                print(f"Специальности добавлены: {new_specialties}")
            except:
                print(f'Что-то пошло не так при добавлении записей специальностей в БД')
        else:
            print(f"Нет новых специальностей для добавления")

        # Добавление новых кампаний в БД из test_data.py
        all_companies = Company.objects.all()
        new_companies = []

        for company in companies:
            try:
                all_companies.get(title=company['title'])
            except models.ObjectDoesNotExist as ex:
                print(ex)
                new_companies.append(Company(
                    title=company['title'],
                    employee_count=int(company['employee_count']),
                    location=company['location'],
                    description=company['description'],
                )
                )
                print(f"Company {company['title']} added!")
        if new_companies:
            try:
                Company.objects.bulk_create(new_companies)
                print(f"Компании успешно добавлены: {new_companies}")
            except:
                print(f'Что-то пошло не так при добавлении записей специальностей в БД')
        else:
            print(f"Нет новых компаний для добавления")

        # Добавляем новые вакансии из test_data.py

        all_vacancy = Vacancy.objects.all()
        new_vacancies = []

        for vacancy in jobs:
            try:
                all_vacancy.get(pk=int(vacancy['id']))
            except models.ObjectDoesNotExist as ex:
                print(ex)
                new_vacancies.append(Vacancy(
                    title=vacancy['title'],
                    company=Company.objects.get(pk=int(vacancy['company'])),
                    specialty=Specialty.objects.get(code=vacancy['specialty']),
                    skills=vacancy['skills'],
                    description=vacancy['description'],
                    salary_min=int(vacancy['salary_from']),
                    salary_max=int(vacancy['salary_to']),
                    published_at=vacancy['posted'],
                    is_publish=True,
                )
                )
                print(f"Vacancy {vacancy['title']} added!")
        if new_vacancies:
            try:
                Vacancy.objects.bulk_create(new_vacancies)
                print(f"Вакансии успешно добавлены: {new_vacancies}")
            except:
                print(f'Что-то пошло не так при добавлении записей вакансий в БД')
        else:
            print(f"Нет новых вакансий для добавления")
