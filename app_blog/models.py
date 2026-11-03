from django.db import models

class AssetCategory(models.Model):
    """Категорія основних засобів"""
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")

    def __str__(self):
        return self.name


class FixedAsset(models.Model):
    """Картка основного засобу (ОЗ)"""
    STATUS_CHOICES = [
        ('active', 'В експлуатації'),
        ('transferred', 'Переміщено'),
        ('disposed', 'Вибув'),
    ]

    inventory_number = models.CharField(max_length=50, unique=True, verbose_name="Інвентарний номер")
    name = models.CharField(max_length=200, verbose_name="Назва основного засобу")
    category = models.ForeignKey(AssetCategory, on_delete=models.SET_NULL, null=True, verbose_name="Категорія")
    initial_cost = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Первісна вартість (грн)")
    acquisition_date = models.DateField(verbose_name="Дата надходження")
    useful_life_months = models.IntegerField(verbose_name="Строк корисного використання (міс.)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Статус")

    def __str__(self):
        return f"[{self.inventory_number}] {self.name}"


class AssetOperation(models.Model):
    """Господарські операції та первинні документи (надходження, переміщення, амортизація, вибуття)"""
    OPERATION_TYPES = [
        ('receipt', 'Надходження ОЗ'),
        ('transfer', 'Переміщення ОЗ'),
        ('depreciation', 'Нарахування амортизації'),
        ('disposal', 'Вибуття / Списання'),
    ]

    asset = models.ForeignKey(FixedAsset, on_delete=models.CASCADE, verbose_name="Основний засіб")
    operation_type = models.CharField(max_length=30, choices=OPERATION_TYPES, verbose_name="Тип операції")
    date = models.DateField(verbose_name="Дата операції")
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Сума (грн)")
    accounting_entry = models.CharField(max_length=100, verbose_name="Бухгалтерська проводка (напр. Дт 10 - Кт 15)")
    document_notes = models.TextField(blank=True, null=True, verbose_name="Підстава / Первинний документ")

    def __str__(self):
        return f"{self.get_operation_type_display()} — {self.asset.name} ({self.date})"
