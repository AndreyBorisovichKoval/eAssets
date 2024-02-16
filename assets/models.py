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
    name = models.CharField(max_length=100)


class Division(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Position(models.Model):
    name = models.CharField(max_length=100)


class Staff(models.Model):
    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    memo = models.TextField()


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


class AssetType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AssetAssignment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    assignment_date = models.DateField()
    return_date = models.DateField(null=True)


class AssetTransfer(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    from_staff = models.ForeignKey(Staff, related_name='transferred_assets', on_delete=models.CASCADE)
    to_staff = models.ForeignKey(Staff, related_name='received_assets', on_delete=models.CASCADE)
    transfer_date = models.DateField()

    def __str__(self):
        return f"{self.asset} transferred from {self.from_staff} to {self.to_staff} on {self.transfer_date}"


# for Migrations
# python manage.py makemigrations
# python manage.py makemigrations assets
# python manage.py migrate



# select * from assets_asset;
#
# INSERT INTO assets_asset (inventory_number, title, identifier, acquisition_date, service_life, cost, current_cost, last_recalculation_date, description)
# VALUES
#     ('INV001', 'Laptop', 'LT001', '2022-01-01', 5, 1000.00, 900.00, '2023-01-01', 'This is a laptop.'),
#     ('INV002', 'Printer', 'PR001', '2022-02-01', 3, 500.00, 450.00, '2023-02-01', 'This is a printer.'),
#     ('INV003', 'Monitor', 'MN001', '2022-03-01', 7, 2000.00, 1800.00, NULL, 'This is a monitor.'),
#     ('INV004', 'Desk', 'DS001', '2022-04-01', 10, 300.00, 270.00, '2023-04-01', 'This is a desk.'),
#     ('INV005', 'Chair', 'CH001', '2022-05-01', 8, 150.00, 135.00, '2023-05-01', 'This is a chair.'),
#     ('INV006', 'Server', 'SV001', '2022-06-01', 6, 2500.00, 2250.00, NULL, 'This is a server.'),
#     ('INV007', 'Keyboard', 'KB001', '2022-07-01', 4, 50.00, 45.00, '2023-07-01', 'This is a keyboard.'),
#     ('INV008', 'Mouse', 'MS001', '2022-08-01', 3, 25.00, 22.50, '2023-08-01', 'This is a mouse.'),
#     ('INV009', 'Projector', 'PJ001', '2022-09-01', 5, 800.00, 720.00, NULL, 'This is a projector.'),
#     ('INV010', 'Scanner', 'SC001', '2022-10-01', 4, 200.00, 180.00, '2023-10-01', 'This is a scanner.'),
#     ('INV011', 'Hard Drive', 'HD001', '2022-11-01', 2, 100.00, 90.00, '2023-11-01', 'This is a hard drive.'),
#     ('INV012', 'Headphones', 'HP001', '2022-12-01', 3, 75.00, 67.50, NULL, 'This is a pair of headphones.'),
#     ('INV013', 'Tablet', 'TB001', '2023-01-01', 4, 400.00, 360.00, '2024-01-01', 'This is a tablet.'),
#     ('INV014', 'Smartphone', 'SP001', '2023-02-01', 2, 600.00, 540.00, '2024-02-01', 'This is a smartphone.'),
#     ('INV015', 'Camera', 'CM001', '2023-03-01', 5, 1000.00, 900.00, NULL, 'This is a camera.'),
#     ('INV016', 'External Hard Drive', 'EHD001', '2023-04-01', 3, 150.00, 135.00, '2024-04-01', 'This is an external hard drive.'),
#     ('INV017', 'Printer Ink', 'PI001', '2023-05-01', 1, 50.00, 45.00, '2024-05-01', 'This is printer ink.'),
#     ('INV018', 'Table Lamp', 'TL001', '2023-06-01', 2, 30.00, 27.00, NULL, 'This is a table lamp.')


# INSERT INTO assets (
#     inventory_number,
#     title,
#     identifier,
#     acquisition_date,
#     service_life,
#     cost,
#     current_cost,
#     description
# ) VALUES
#     ('123456789', 'Ноутбук', 'e2345678-e234-4e23-a456-789012345678', '2023-01-01', 5, 100000.00, 80000.00, 'Ноутбук Lenovo ThinkPad X1 Carbon Gen 10'),
#     ('987654321', 'Смартфон', 'f2345678-f234-4f23-b456-789012345678', '2023-03-08', 3, 50000.00, 40000.00, 'Смартфон Samsung Galaxy S23 Ultra'),
#     ('345678901', 'Планшет', 'c2345678-c234-4c23-c456-789012345678', '2023-05-15', 2, 30000.00, 25000.00, 'Планшет Apple iPad Air 5'),
#     ('456789012', 'Сервер', 'd2345678-d234-4d23-d456-789012345678', '2023-07-22', 10, 500000.00, 400000.00, 'Сервер Dell PowerEdge R750'),
#     ('567890123', 'Принтер', 'e2345678-e234-4e23-e456-789012345678', '2023-09-09', 5, 20000.00, 15000.00, 'Принтер HP LaserJet Pro M404dn'),
#     ('678901234', 'Монитор', 'f2345678-f234-4f23-f456-789012345678', '2023-11-16', 3, 10000.00, 8000.00, 'Монитор Dell U2422HE'),
#     ('789012345', 'Клавиатура', 'g2345678-g234-4g23-g456-789012345678', '2024-01-03', 2, 5000.00, 4000.00, 'Клавиатура Logitech MX Keys Mini'),
#     ('890123456', 'Мышь', 'h2345678-h234-4h23-h456-789012345678', '2024-03-10', 2, 3000.00, 2500.00, 'Мышь Logitech MX Master 3S'),
#     ('901234567', 'Наушники', 'i2345678-i234-4i23-i456-789012345678', '2024-05-17', 2, 10000.00, 8000.00, 'Наушники Sony WH-1000XM5'),
