from django.contrib import admin
from .models import Application, Specialty, Company, Vacancy

admin.site.register(Application)
admin.site.register(Specialty)
admin.site.register(Company)
admin.site.register(Vacancy)
