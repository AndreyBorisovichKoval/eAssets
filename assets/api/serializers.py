from rest_framework import serializers
from assets.models import Department, Division, Position, Staff, EmployeeDetails, Asset, AssetAssignment


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetails
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAssignment
        fields = '__all__'


# class Department(models.Model):
# class Division(models.Model):
# class Position(models.Model):
# class Staff(models.Model):
# class EmployeeDetails(models.Model):
# class Asset(models.Model):
# class AssetAssignment(models.Model):
