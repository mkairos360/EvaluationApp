# Generated by Django 4.0.1 on 2022-03-20 08:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_course_slug_alter_evaluation_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('ea5fdbb8-5034-4b48-b2a3-ff148eb82f9c'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('c2385f4a-077b-4494-8768-7b82cb0da389'), null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.UUID('5ebdf803-dc8a-4064-82b5-b8f1660142a3'), null=True, unique=True),
        ),
    ]