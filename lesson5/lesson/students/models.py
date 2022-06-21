from tabnanny import verbose
from django.db import models


class StudentGroup(models.Model):

    name = models.CharField(verbose_name='Группа',
                            max_length=100, null=True, blank=True)
    sudents_number = models.IntegerField(
        verbose_name='Количество студентов', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Группа студентов"
        verbose_name_plural = "Группы студентов"


class Student(models.Model):

    SURNAME_CHOICES = {
        ('Petrenko', 'Петренко'),
        ('Ivanenko', 'Іваненко'),
    }

    name = models.CharField(verbose_name='Имя', max_length=100)
    surname = models.CharField(
        verbose_name='Фамилия', max_length=50, null=True, blank=True, choices=SURNAME_CHOICES)
    birthdate = models.DateField(
        verbose_name='День рождения', null=True, blank=True)
    group = models.ForeignKey(StudentGroup, verbose_name='Группа',
                              on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

        class Meta:
            verbose_name = "Студент"
            verbose_name_plural = "Студенты"
