from django.contrib import admin

from assets.models import Department, Division, Position, Staff, EmployeeDetails, Asset, AssetAssignment

admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(EmployeeDetails)
admin.site.register(Asset)
admin.site.register(AssetAssignment)
