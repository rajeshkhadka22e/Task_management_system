# # from django.contrib import admin

# # from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import TaskList, Task

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'due_date', 'task_list', 'created_at')  # Fields to display in the list view
#     list_filter = ('status', 'due_date')  # Filters for the admin sidebar
#     search_fields = ('title', 'description')  # Fields to search in the admin

# class TaskListAdmin(admin.ModelAdmin):
#     list_display = ('name', 'created_at')  # Fields to display for TaskList
#     search_fields = ('name',)  # Search by TaskList name

# # Register the models with the custom admin classes
# admin.site.register(TaskList, TaskListAdmin)
# admin.site.register(Task, TaskAdmin)

# SAM'S AREA
# frontend/admin.py

from django.contrib import admin
from .models import TaskList, Task,UserProfile, TeamMember,Project,User

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'budget_amount', 'task_duration','task_list', 'created_at')  # Ensure these fields exist in the Task model
    list_filter = ('status', 'due_date')  # Ensure these fields exist in the Task model
    search_fields = ('title', 'description')  # Ensure these fields exist in the Task model

class TaskListAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Ensure these fields exist in the TaskList model
    search_fields = ('name',)  # Ensure this field exists in the TaskList model

# Register the models with the custom admin classes
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(Task, TaskAdmin)


# Customize how the UserProfile is displayed in the admin panel
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role' ,'experienced')  # Display these fields in the admin list view
    search_fields = ('name', 'email')  # Allow searching by name or email
    list_filter = ('role',)  # Add filtering options based on role

# Register the UserProfile model with its customized admin view
admin.site.register(UserProfile, UserProfileAdmin)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'experience', 'email')
    search_fields = ('name', 'role', 'email')



# Register the Project model with the admin site
admin.site.register(Project)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'role', 'experience', 'email')
    search_fields = ('first_name', 'role', 'email')


from django.contrib import admin
from .models import Event

# Register the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title',)
    list_filter = ('start_date', 'end_date')
