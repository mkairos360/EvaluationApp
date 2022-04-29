# Generated by Django 4.0.1 on 2022-03-20 08:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_course_slug_alter_evaluation_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('abbb255e-6ca3-49d1-9e5b-79f087c6ff81'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('f611a624-6972-45bb-a2fa-6aa41ca0e4c4'), null=True, unique=True),
        ),
    ]