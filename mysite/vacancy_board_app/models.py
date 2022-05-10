from django.contrib.auth.models import User
from django.db import models

from mysite.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.IntegerField(default=0)
    salary_max = models.IntegerField(default=0)
    published_at = models.DateField()
    is_publish = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-published_at']

    def __str__(self):
        return f"{self.title}"


class Company(models.Model):
    title = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.PositiveIntegerField(default=1)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='company')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['pk']

    def __str__(self):
        return f"{self.title}"


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    picture = models.URLField(default='https://place-hold.it/100x60')

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'
        ordering = ['pk']

    def __str__(self):
        return f"{self.code}"


class Application(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        ordering = ['pk']

    def __str__(self):
        return f"{self.name}"
