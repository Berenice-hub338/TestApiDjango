from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class Usermanager(BaseUserManager):
    def create_user(self, email, username, telephone, password=None):
        if not email or not username or not telephone:
            raise ValueError("Veuillez remplir tous les chapms!")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, telephone=telephone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, telephone, password=None):
        user = self.create_user(email, username, telephone, password)
        user.is_staff = True
        user.is_active=True
        user.is_superuser = True
        user.save()
        return user
        

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    telephone = models.CharField(max_length=255)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = Usermanager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'telephone']

    def __str__(self):
        return self.email

