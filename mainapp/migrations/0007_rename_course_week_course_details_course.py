# Generated by Django 4.1.6 on 2023-02-06 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_course_course_details_course_week'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_details',
            old_name='Course_week',
            new_name='Course',
        ),
    ]