from django.contrib import admin

# from assets.models import UserManager, User, Department, Division, Position, Staff, Asset, AssetType, AssetAssignment, AssetTransfer
from assets.models import Department, Division, Position, Staff, Asset, AssetType, AssetAssignment


# admin.site.register(UserManager)
# admin.site.register(User)
admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(AssetAssignment)
# admin.site.register(AssetTransfer)

