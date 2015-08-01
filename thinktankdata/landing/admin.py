from django.contrib import admin

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text','pub_date']
    list_display_links = ['id',]
    readonly_fields=('id',)
    search_fields = ['question_text',]

