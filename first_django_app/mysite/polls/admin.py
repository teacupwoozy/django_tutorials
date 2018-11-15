from django.contrib import admin

from .models import Choice, Question


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldset = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# Alternate:
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)