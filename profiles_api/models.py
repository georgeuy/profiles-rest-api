from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserProfileManager(BaseUserManager):
    """Manager for users profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("El email es obligatorio")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password=None):
        """Create a new superuser profile"""

        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users int the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Retrieve full name of user """
        return self.name

    def get_short_name(self):
        """ Retrieve short name of user """
        return self.name

    def __str__(self):
        return f"<UserProfile: {self.email}>"
