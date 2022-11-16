from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index, name='index'),
    path("courses/", courses, name="courses"),
    path("coursedetails/<str:pkid>/", coursedetails, name="coursedetails"),
    path("lessons/<str:pkid>/", lessons, name="lessons"),
    path('quiz/', quizess, name='quiz'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)