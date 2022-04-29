# Generated by Django 4.0.1 on 2022-03-29 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_evaluationsubmission_curriculum_feedback_beginning_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='curriculum_feedback_beginning_answer',
            field=models.IntegerField(choices=[(0, 'Not Applicable'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Moderately Disagree'), (4, 'Agree'), (5, 'Strongly Agree')], default=None),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='curriculum_feedback_books_answer',
            field=models.IntegerField(choices=[(0, 'Not Applicable'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Moderately Disagree'), (4, 'Agree'), (5, 'Strongly Agree')], default=None),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='curriculum_feedback_course_answer',
            field=models.IntegerField(choices=[(0, 'Not Applicable'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Moderately Disagree'), (4, 'Agree'), (5, 'Strongly Agree')], default=None),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='curriculum_feedback_lecture_answer',
            field=models.IntegerField(choices=[(0, 'Not Applicable'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Moderately Disagree'), (4, 'Agree'), (5, 'Strongly Agree')], default=None),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='curriculum_feedback_outcomes_answer',
            field=models.IntegerField(choices=[(0, 'Not Applicable'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Moderately Disagree'), (4, 'Agree'), (5, 'Strongly Agree')], default=None),
        ),
        migrations.AlterField(
            model_name='evaluationsubmission',
            name='curriculum_feedback_procedures_answer',
            field=models.IntegerField(choices=[(0, 'Not Applicable'), (1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Moderately Disagree'), (4, 'Agree'), (5, 'Strongly Agree')], default=None),
        ),
    ]