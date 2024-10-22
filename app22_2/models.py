
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100, null=True)
    rollno=models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
