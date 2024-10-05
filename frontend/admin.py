# from django.contrib import admin

# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TaskList, Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'task_list', 'created_at')  # Fields to display in the list view
    list_filter = ('status', 'due_date')  # Filters for the admin sidebar
    search_fields = ('title', 'description')  # Fields to search in the admin

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Fields to display for TaskList
    search_fields = ('name',)  # Search by TaskList name

# Register the models with the custom admin classes
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)

