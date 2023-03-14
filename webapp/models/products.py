from django.db import models
from django.db.models import TextChoices
from django.utils import timezone
from django.core.validators import MinValueValidator


class CategoryChoice(TextChoices):
    OTHER = 'OTHER', 'Разное'
    FOOD = 'FOOD', 'Еда'
    CAR = 'CAR', 'Автомобиль'


class Product(models.Model):
    category = models.CharField(verbose_name="Категория", choices=CategoryChoice.choices, max_length=20,
                                default=CategoryChoice.OTHER, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание")
    photo = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Фото")
    count = models.IntegerField(validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")
    deleted_at = models.DateTimeField(verbose_name="Время и дата удаления", null=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.description}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
