# Generated by Django 3.1.3 on 2022-11-01 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('varlmsapp', '0011_auto_20221101_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lessons',
            field=models.ManyToManyField(to='varlmsapp.Lessons'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answer',
            field=models.IntegerField(choices=[(1, models.CharField(max_length=100)), (2, models.CharField(max_length=100)), (3, models.CharField(max_length=100)), (4, models.CharField(max_length=100))], max_length=100),
        ),
    ]