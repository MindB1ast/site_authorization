from django.db import models
from django.contrib.auth.models import User
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    user = models.ManyToManyField(User, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class CourseElement(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self) -> str:
        return self.name