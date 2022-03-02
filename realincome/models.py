from django.db import models
from users.models import User

# Create your models here.
class Income(models.Model):
    SOURCE_OPTIONS =[
        ('SALARY','SALARY'),
        ('BUSINESS','BUSINESS'),
        ('SIDE-HUSTLES','SIDE_HUSTLES'),
        ('OTHERS','OTHERS')]
    
    source= models.CharField(choices= SOURCE_OPTIONS, max_length=220)
    amount= models.IntegerField()
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField(null= True, blank= True)

    def __str__(self):
        return self.owner+'s name'

class EmployeeSalary(models.Model):
    salary_per_hour= models.IntegerField()
    working_hour = models.IntegerField()
    allowance = models.IntegerField()