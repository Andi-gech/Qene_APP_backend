# Generated by Django 4.1.6 on 2023-02-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_questions_code_alter_questions_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
    ]
