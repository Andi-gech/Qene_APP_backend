# Generated by Django 4.1.6 on 2023-02-06 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_questions_quiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_details',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='course_outlines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_module_name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.course')),
            ],
        ),
    ]
