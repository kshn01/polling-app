from django.contrib import admin
from django.contrib.admin.helpers import InlineAdminForm
from django.contrib.admin.options import StackedInline

from .models import Question, Choice

# Register your models here.


# todo creating custom form inside the admin panel of django



class ChoiceInline(admin.TabularInline):  # tabularinline or stackedInline are just layouts
    model= Choice
    extra = 3



class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),

        ('Date Information',{
            'fields':['pub_date'],
            'classes':['collapse'], # if you want to collapse this(particularly date information) fieldset  
        }),  
    ]

    inlines =[ChoiceInline]

    list_display = ('question_text', 'pub_date',  'was_published_recently')

    list_filter  = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question,QuestionAdmin)