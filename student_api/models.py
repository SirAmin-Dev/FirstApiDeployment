from django.db import models

# Create your models here.
class Student(models.Model):
    names = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.names