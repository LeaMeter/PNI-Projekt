# Generated by Django 3.1.5 on 2021-01-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorski', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnici',
            name='role',
            field=models.CharField(choices=[('mentor', 'mentor'), ('student', 'student')], default='student', max_length=20, verbose_name='role'),
        ),
    ]
