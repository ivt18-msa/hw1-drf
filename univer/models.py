from tabnanny import verbose
from django.db import models


class Student(models.Model):
    last_name = models.CharField('фамилия', max_length=50)
    first_name = models.CharField('имя', max_length=50)
    second_name = models.CharField('отчество', max_length=50, blank=True, default='')
    id_number = models.CharField('номер студбилета', max_length=25)

    def __str__(self):
        res = self.last_name + ' ' + self.first_name[0] + '.'
        if self.second_name:
            res += self.second_name[0] + '.'
        return res

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
