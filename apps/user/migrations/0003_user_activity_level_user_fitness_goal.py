# Generated by Django 4.2.13 on 2024-05-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_age_user_gender_user_height_user_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activity_level',
            field=models.CharField(blank=True, choices=[('0', '주 0회'), ('1-2', '주 1-2회'), ('3-4', '주 3-4회'), ('5-7', '주 5-7회')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='fitness_goal',
            field=models.CharField(blank=True, choices=[('muscle_gain', '근성장'), ('diet', '다이어트'), ('bulk_up', '벌크업')], max_length=20, null=True),
        ),
    ]
