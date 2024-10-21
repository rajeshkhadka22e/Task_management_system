from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


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

    # task_duration = models.CharField(max_length=20, blank=True)  # Duration of the task (changed from 'duration')
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2, default='0.00')  # Budget amount (changed from 'budget')
   

    role = models.CharField(max_length=100, default='Member')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    due_date = models.DateField(default=timezone.now)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    task_duration = models.IntegerField() 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_overdue(self):
        return self.due_date < timezone.now().date() and self.status!= 'completed'

    def __str__(self):
        return self.title




class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    experienced = models.CharField(max_length=10,default=1)
    email = models.EmailField(unique=True)
    role_choices = [
        ('Developer', 'Developer'),
        ('Manager', 'Manager'),
        ('Designer', 'Designer'),
    ]
    role = models.CharField(max_length=50, choices=role_choices, default='Developer')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('Manager', 'Team Manager'),
        ('Developer', 'Developer'),
        ('Qa', 'QA Engineer'),
    ]
    
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='Developer',choices=ROLE_CHOICES)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    working_projects = models.CharField(max_length=200,default='null')
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.name
    


class Project(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    




######user model######
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    experience = models.IntegerField(default=0)  # Experience in years
    role = models.CharField(max_length=50)  # Role of the user
    email = models.EmailField(unique=True)
    profile_images = models.ImageField(upload_to='profiles/', blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.email.split('@')[0])
        super().save(*args, **kwargs)

    
    from django.db import models





###########calender event dynamic########
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Optional end date

    def __str__(self):
        return self.title
