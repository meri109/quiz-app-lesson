from django.contrib import admin
from . import models
from .models import Question, QuizResult, Option
# Register your models here.



class OptionInline(admin.TabularInline):
    model = models.Option


@admin.register(models.Question)   
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
          

admin.site.register(QuizResult)
