from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


def get_file_name(_, filename):
    now = timezone.now()
    return '/'.join(['tmp', 'y-month', f'{now.year}-{now.month}', filename])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to=get_file_name, null=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    CURRENCIES = (
        ('$', 'USD'),
        ('֏', 'AMD'),
    )

    name = models.CharField(max_length=100)
    vin = models.CharField(max_length=17, null=True, blank=True, unique=True, help_text='Vehicle Identification Number')

    price = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(max_length=1, choices=CURRENCIES)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2022)])

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='cars_images', null=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'cars'

    def __str__(self) -> str:
        return self.name
