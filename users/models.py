import email
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin,BaseUserManager)

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username , email, password=None):
        if username is None:
            raise TypeError('User shoul have username')
        if email is None:
            raise TypeError("user should have email")

        user= self.model(username=username, email= self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def Create_superuser(self , username, email ,password=None):
        if password is None:
            raise TypeError("Password cann't be none")
        user=self.create_user()


class User( AbstractBaseUser , PermissionsMixin ):
    username = models.CharField(max_length=220, unique=True, db_index=True)
    email= models.EmailField(max_length=220,unique=True,db_index=True)
    is_verified =models.BooleanField(default=False)
    is_active =models.BooleanField(default=True)
    is_satff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects= UserManager()

    def __strt__(self):
        return self.email

    def 