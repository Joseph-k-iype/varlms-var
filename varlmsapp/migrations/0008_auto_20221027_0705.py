# Generated by Django 3.1.3 on 2022-10-27 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varlmsapp', '0007_remove_course_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(to='varlmsapp.lessons'),
        ),
        migrations.AddField(
            model_name='lessons',
            name='lessonindex',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='lessonsOfCourse',
        ),
    ]
