from django.db import models
from users.models import User
# Create your models here.
class ActaulExpense(models.Model):
    CATEGORY_CHOICES =[
        ('FOOD','FOOD'),
        ('RENT','RENT'),
        ('TRAVEL','TRAVEL'),
        ('OTHER','OTHER')]
    
    category= models.CharField(choices=CATEGORY_CHOICES, max_length=220)
    amount= models.DecimalField(max_digits=10, decimal_places=2 )
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date= models.DateField()

    def __str__(self):
        return self.owner+'s income'