# Generated by Django 4.0.3 on 2022-05-07 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0004_category_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='duration',
            field=models.IntegerField(help_text='Time in minutes', null=True),
        ),
        migrations.AddField(
            model_name='reponse',
            name='correct',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='reponse',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.questions'),
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
