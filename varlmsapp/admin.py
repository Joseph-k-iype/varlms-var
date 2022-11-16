from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Course)
admin.site.register(Lessons)
admin.site.register(quiz)
admin.site.register(coursestaken)
admin.site.site_header  =  "Varghese admin"  
admin.site.site_title  =  "Varghese admin site"
admin.site.index_title  =  "Varghese Admin"