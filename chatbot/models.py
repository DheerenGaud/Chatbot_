from django.db import models

# Create your models here.
class Newevent(models.Model):
    event=models.CharField(max_length=122)
    eventurl=models.URLField()
    eventstart=models.DateTimeField()
    discription=models.CharField(max_length=122)
    eventend=models.DateTimeField()
    eventlogo=models.CharField(max_length=122)
    
    def __str__(self) -> str:
        return self.event
    
class Collageinfo(models.Model):
    collagename=models.CharField(max_length=122)
    achivment=models.CharField(max_length=122)
    collageurl=models.URLField()
    detail=models.CharField(max_length=1000)
   
    def __str__(self) -> str:
        return self.collagename
    

class Deparment(models.Model):
    department_name = models.CharField(max_length=50)
    department_hod_name = models.CharField(max_length=100)
    department_teachingstaff = models.IntegerField()
    department_nonteachingstaff = models.IntegerField()
    department_fees = models.IntegerField()
    def _str_(self):
        return self.department_name    