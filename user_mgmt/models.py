# accounts/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):

    """
    CustomUserManager class inherits BaseUserManager which manages both user and superuser
    BaseUserManager has several methods in it and create_user and super_user is few of methods exist
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Method to create an user
        :param email:
        :param password:
        :param extra_fields:
        :return:User
        """
        if not email:
            raise ValueError('The Email Field must be set')

        if not password:
            raise ValueError('The password field is empty')

        email = self.normalize_email(email)

        # Below line creates an instance of object(CustomUser)
        user = self.model(email=email, **extra_fields)

        # This will hash password
        user.set_password(password)

        # Saves user instance to db
        user.save(using=self._db)
        return user

    def create_superuser(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):

    """
    class to specify  fields of customuser
    AbstractBaseUser is class which contains most of the fields of User model
    PermissionsMixin is a class which deals with permissions of groups and individuals
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # creating an instance of CustomUserManager
    # When creating an user code should like below
    # CustomUser.objects.create_user(email,password)
    # object is an instance of CustomerUserManager . so it inherits methods in CustomerUserManager
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.user.username
