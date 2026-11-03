from django.contrib import admin
from .models import AssetCategory, FixedAsset, AssetOperation

admin.site.register(AssetCategory)
admin.site.register(FixedAsset)
admin.site.register(AssetOperation)