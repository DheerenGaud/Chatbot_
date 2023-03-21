from django.db import models

# Create your models here.
class Contact(models.Model):
    Fname=models.CharField(max_length=122)
    Lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    
    def __str__(self) -> str:
        return self.Fname
  