from django.db import models

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
    department_teachingstaff = models.IntegerField(null=True)
    department_nonteachingstaff = models.IntegerField(null=True)
    department_fees = models.IntegerField(null=True)
    admission_cutoff = models.IntegerField(default=1)
    admission_capacity = models.IntegerField(default=1)
    admission_detail=models.CharField(max_length=1000,default="null")
    
    def _str_(self)  -> str:
        return self.department_name   
    
    
class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=100)
    scholarship_documents =models.TextField(null=True)
    scholarship_contact = models.IntegerField(null=True)
    scholarship_dsiscription = models.TextField(null=True)
   
    def _str_(self)  -> str:
        return self.scholarship_name    