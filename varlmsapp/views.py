from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required
def courses(request):
    course = Course.objects.all()
    print(course)
    # courses = Course.objects.get(id=id)
    # topics = topic.objects.filter(course=course)
    user = User.objects.get(username=request.user)
    courses_taken = coursestaken.objects.filter(user=user)
    courses_not_taken = Course.objects.exclude(coursestaken__user=user)

    return render(request, 'courses.html', {'course': course, 'courses_taken': courses_taken, 'courses_not_taken': courses_not_taken})


@login_required
def coursedetails(request, pkid):
    course = Course.objects.filter(id=pkid)
    return render(request, 'coursedetails.html', {'course': course})


@login_required
def lessons(request, pkid):
    course = Course.objects.filter(id=pkid).get()
    lessons = list(course.lessons.order_by('lessonindex').values())

    #get the quiz for a particular lesson
    for i in range(len(lessons)):
        current = lessons[i]
        print(type(current))
        quizForLesson = list(quiz.objects.filter(lesson=current['id']).values())
        current["quiz"] = quizForLesson
        lessons[i] = current
        print(quizForLesson)

    return render(request, 'lessons.html', {'course': course, 'lessons': lessons, })

def quizess(request):
    return render(request, 'quiz.html')
@login_required
def addlesson(request):
    form = AddLessonForm(request.POST, request.FILES)
    if form.is_valid():
        print(form.data)
        course = Course.objects.filter(id = form.data["course"]).get()

        # take size of the lessons

        lessonIndex = len(list(course.lessons.all()))
        # make that size as index of new lesson
        # save new lesson
        newLesson = Lessons(
            lessonname= form.data["lessonname"],
            description = form.data["description"],
            video = request.FILES["video"],
            lessonindex = lessonIndex
        )
        newLesson.save()
        # add the new lesson to the many to many field of course
        course.lessons.add(newLesson)
        course.save()
        return(redirect("/admin/varlmsapp/lessons"))
        # save course
    return render(request, 'addlessons.html', {'form':form})
