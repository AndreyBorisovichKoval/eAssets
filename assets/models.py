from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE


class Department(models.Model):
    name = models.CharField(max_length=100)


class Division(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Position(models.Model):
    name = models.CharField(max_length=100)


class Staff(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    employee_details = models.OneToOneField("EmployeeDetails", on_delete=models.CASCADE)


class EmployeeDetails(models.Model):
    date_of_birth = models.DateField(blank=True, null=True)
    passport = models.CharField(max_length=12)
    individual_taxpayer_number = models.CharField(max_length=12)
    gender = models.CharField(max_length=10, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    education = models.TextField(blank=True)
    courses = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    language_skills = models.TextField(blank=True, null=True)
    previous_employment = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_number = models.CharField(max_length=20, blank=True)
    joining_date = models.DateField(blank=True, null=True)
    contract_start_date = models.DateField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
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



class AssetAssignment(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    assignment_date = models.DateField()
    return_date = models.DateField(null=True)


# for Migrations
# python manage.py makemigrations
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
