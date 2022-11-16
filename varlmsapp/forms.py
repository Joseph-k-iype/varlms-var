
from statistics import mode
from django import forms
from .models import *
# creating a form


class AddLessonForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects
    )
    lessonname = forms.CharField()
    description = forms.CharField()
    video = forms.FileField()
