# Generated by Django 4.1.7 on 2024-03-22 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0003_choice_question_quiz_useranswer_question_quiz_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useranswer',
            name='user',
        ),
        migrations.AddField(
            model_name='useranswer',
            name='student_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentprofile.studentprofile'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentprofile.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentprofile.quiz'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentprofile.question'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='selected_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentprofile.choice'),
        ),
    ]
