from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import validate_email
class CustomUserManager(UserManager):

    def _get_email(self, email: str):
        validate_email(email)
        return self.normalize_email(email)

    def _create_user(
        self, 
        email: str, 
        password: str, 
        is_staff: bool = False, 
        is_superuser: bool = False
    ):
        
        email = self._get_email(email)
        
        user = User(email=email, username=email, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, email: str, password: str):
        return self._create_user(email, password, is_staff=True, is_superuser=True)
    
    def create_user(self, email: str, password: str):
        return self._create_user(email, password)

class User(AbstractUser):

    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()