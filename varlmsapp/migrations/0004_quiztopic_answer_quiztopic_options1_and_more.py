# Generated by Django 4.1.2 on 2022-10-25 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varlmsapp', '0003_lessons_lessonname'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztopic',
            name='answer',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiztopic',
            name='options1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiztopic',
            name='options2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiztopic',
            name='options3',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiztopic',
            name='options4',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiztopic',
            name='quizname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]