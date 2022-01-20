from tabnanny import verbose
from django.db import models


class Student(models.Model):
    last_name = models.CharField('фамилия', max_length=50)
    first_name = models.CharField('имя', max_length=50)
    second_name = models.CharField('отчество', max_length=50, blank=True, default='')
    id_number = models.CharField('номер студбилета', max_length=25)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
