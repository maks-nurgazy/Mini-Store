from PIL import Image
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=256, help_text="Description for category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 300:
            size = (400, 300)
            img.thumbnail(size)
            img.save(self.image.path)

    def __str__(self):
        return self.name
