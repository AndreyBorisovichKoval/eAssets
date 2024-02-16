from rest_framework import serializers
# from assets.models import (UserManager, User, Department, Division, Position, Staff, Asset, AssetType, AssetAssignment, AssetTransfer)
from assets.models import Department, Division, Position, Staff, Asset, AssetType, AssetAssignment


# class UserManagerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserManager
#         fields = '__all__'
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


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


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetType
        fields = '__all__'


class AssetAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetAssignment
        fields = '__all__'


# class AssetTransferSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AssetTransfer
#         fields = '__all__'


# class UserManger(models.Model):
# class User(models.Model):
# class Department(models.Model):
# class Division(models.Model):
# class Position(models.Model):
# class Staff(models.Model):
# class Asset(models.Model):
# class AssetAssignment(models.Model):
# admin.site.register(AssetType)
# admin.site.register(AssetAssignment)
# admin.site.register(AssetTransfer)
