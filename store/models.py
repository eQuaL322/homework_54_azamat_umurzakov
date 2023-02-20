from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name="Наименование")
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание", default='')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name="Категория", default=None)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время добавления")
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False, verbose_name="Цена")
    image = models.URLField(max_length=1000, blank=False, null=False, verbose_name="Ссылка на изображение")

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name="Наименование")
    description = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.title} - {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
