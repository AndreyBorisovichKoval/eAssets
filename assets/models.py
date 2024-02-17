from django.db import models
from django.contrib.auth.models import User
# from django.db.models import CASCADE
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# class UserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         if not username:
#             raise ValueError('Username is required')
#         user = self.model(username=username)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None):
#         return self.create_user(username, password)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_user = models.BooleanField(default=False)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#
#     def __str__(self):
#         return self.username
#

class Department(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)


class Division(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)


class Position(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)


class Staff(models.Model):
    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    memo = models.TextField()
    is_deleted = models.BooleanField(default=False)


class Asset(models.Model):
    inventory_number = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    identifier = models.CharField(max_length=120)
    acquisition_date = models.DateField()
    service_life = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    current_cost = models.DecimalField(max_digits=10, decimal_places=2)
    last_recalculation_date = models.DateField(null=True)
    description = models.TextField(null=True)
    asset_type = models.ForeignKey('AssetType', on_delete=models.CASCADE)
    is_written_off = models.BooleanField(default=False)


class AssetType(models.Model):
    title = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class AssetAssignment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    assignment_date = models.DateField()
    return_date = models.DateField(null=True)


# for Migrations
# python manage.py makemigrations
# python manage.py makemigrations assets
# python manage.py migrate


