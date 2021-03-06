from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
import datetime

class MyAccountManager(UserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=20, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
        
class Case(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField(verbose_name='Date of Birth')
    accounts = models.ManyToManyField(Account, related_name="cases", through='CaseLink')

    def __str__(self):
        return f'{self.id}: {self.name}, {self.dob}'

class CaseLink(models.Model):
    account = models.ForeignKey(Account, related_name="caselink", on_delete=models.CASCADE)
    case = models.ForeignKey(Case, related_name="caselink", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'

class Incident(models.Model):
    antecedent = models.CharField(max_length=60)
    behavior = models.CharField(max_length=60)
    consequence = models.CharField(max_length=60)
    case = models.ForeignKey(Case, related_name="incidents", on_delete=models.CASCADE)
    date = models.DateField(verbose_name="Date of Incident")
    time = models.TimeField(verbose_name="Time of Incident")

    def __str__(self):
        return f'A: {self.antecedent}, B: {self.behavior}, C: {self.consequence}, {self.date}, {self.time}'