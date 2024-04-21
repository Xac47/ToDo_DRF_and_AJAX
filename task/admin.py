from django.contrib import admin

from .models import Tasks


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
    list_display_links = ('id', 'title', 'completed')
    save_as = True
