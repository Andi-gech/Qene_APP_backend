# Generated by Django 4.1.6 on 2023-02-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_quiz_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_outlines',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
