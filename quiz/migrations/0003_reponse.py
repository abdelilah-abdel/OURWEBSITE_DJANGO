# Generated by Django 4.0.3 on 2022-04-24 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_category_quiz_updated_questions_quiz_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='reponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('questions', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.questions')),
            ],
        ),
    ]
