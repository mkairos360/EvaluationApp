# Generated by Django 4.0.1 on 2022-03-29 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_alter_evaluationsubmission_curriculum_feedback_beginning_answer_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('name', 'level', 'course_group', 'facilitator', 'program')},
        ),
    ]