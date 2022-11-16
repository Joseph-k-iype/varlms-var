from secrets import choice
from django.db import models
# import user model
from django.contrib.auth.models import User
# Create your models here.


class Lessons(models.Model):
    lessonname = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')
    lessonindex = models.IntegerField()

    class Meta:
        db_table = 'lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.lessonname


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.CharField(max_length=100)
    lessons = models.ManyToManyField(Lessons)

    class Meta:
        db_table = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return self.name


class coursestaken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'coursestaken'
        verbose_name_plural = 'coursestaken'

    def __str__(self):
        return self.user.username
# class topictaken(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     topic = models.ForeignKey(topic, on_delete=models.CASCADE)
#     date = models.DateField()

#     class Meta:
#         db_table = 'topictaken'
#         verbose_name_plural = 'topictaken'

#     def __str__(self):
#         return self.user.username + " " + self.topic.name


# a model for assigning an mca quiz with 4 options to a lesson
class quiz(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)   
    answer = models.IntegerField(max_length=100, choices=[(1, option1), (2, option2), (3, option3), (4, option4)])
    class Meta:
        db_table = 'quiz'
        verbose_name_plural = 'quiz'

    def __str__(self):
        return self.question

