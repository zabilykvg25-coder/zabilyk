from django.contrib import admin
from .models import AssetCategory, FixedAsset, AssetOperation

@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(FixedAsset)
class FixedAssetAdmin(admin.ModelAdmin):
    list_display = ('inventory_number', 'name', 'category', 'initial_cost', 'acquisition_date', 'status')
    list_filter = ('status', 'category')
    search_fields = ('inventory_number', 'name')

@admin.register(AssetOperation)
class AssetOperationAdmin(admin.ModelAdmin):
    list_display = ('asset', 'operation_type', 'date', 'amount', 'accounting_entry')
    list_filter = ('operation_type', 'date')
    search_fields = ('asset__name', 'accounting_entry')