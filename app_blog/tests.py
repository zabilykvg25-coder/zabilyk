from django.test import TestCase
from .models import AssetCategory, FixedAsset
from datetime import date

class AssetModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створюємо тестову категорію та основний засіб для перевірки
        category = AssetCategory.objects.create(
            name='Обчислювальна техніка',
            description='ПК та сервери'
        )
        FixedAsset.objects.create(
            inventory_number='INV-999',
            name='Тестовий сервер',
            category=category,
            initial_cost=50000.00,
            acquisition_date=date.today(),
            useful_life_months=60,
            status='active'
        )

    def test_fixed_asset_creation(self):
        asset = FixedAsset.objects.get(inventory_number='INV-999')
        self.assertEqual(asset.name, 'Тестовий сервер')
        self.assertEqual(str(asset), '[INV-999] Тестовий сервер')