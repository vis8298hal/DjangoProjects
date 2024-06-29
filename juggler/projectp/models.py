from django.db import models


# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100, help_text="Contains the name of Project")
    creation_time = models.DateTimeField(auto_now_add=True, help_text="Project creation time.")
    completion_time = models.DateTimeField(null=True, help_text="Project completion time")


    def __str__(self):
        return self.project_name

class Task(models.Model):

    task_name = models.CharField(max_length=70, help_text="Contains the Task Name under Project")
    description = models.TextField(help_text="Task Description")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    time_estimate = models.IntegerField(help_text="Time in hours required to complete task")
    completed = models.BooleanField(default=False, help_text="Status of Task Completion")
    

    def __str__(self):
        return self.task_name
