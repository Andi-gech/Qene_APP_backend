# Generated by Django 4.1.6 on 2023-02-16 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_course_outlines_is_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='course',
            new_name='courseoutlines',
        ),
    ]
