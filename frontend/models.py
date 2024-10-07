
from django.db import models
from django.utils import timezone

class TaskList(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('overdue', 'Overdue'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

#    SAM
    task_duration = models.CharField(max_length=20, default='0')  # Duration of the task (changed from 'duration')
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')  # Budget amount (changed from 'budget')
   
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    due_date = models.DateField(default=timezone.now)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_overdue(self):
        return self.due_date < timezone.now().date() and self.status != 'completed'

    def __str__(self):
        return self.title

# frontend/models.py

from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

