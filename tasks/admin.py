from django.contrib import admin
from tasks.models import Tasks


class TasksAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tasks, TasksAdmin)