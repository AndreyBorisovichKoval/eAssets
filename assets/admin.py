from django.contrib import admin
from assets.models import Department, Division, Position, Staff, Asset, AssetType, AssetAssignment, TaskCheckPoint, UserAction, UserSettings


admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Position)
admin.site.register(Staff)
admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(AssetAssignment)
admin.site.register(TaskCheckPoint)
admin.site.register(UserAction)
admin.site.register(UserSettings)
