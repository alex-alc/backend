# Generated by Django 4.0.5 on 2022-06-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_studentgroup_sudents_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='surname',
            field=models.CharField(blank=True, choices=[('Ivanenko', 'Іваненко'), ('Petrenko', 'Петренко')], max_length=50, null=True, verbose_name='Фамилия'),
        ),
    ]