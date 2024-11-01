from django.db import models

class Product(models.Model):
    stripe_product_id = models.CharField(max_length=255, default="NULL")
    stripe_price_id = models.CharField(max_length=255, default="NULL")
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    products = models.ManyToManyField('Product', related_name='orders')  # Use 'Product' as a string if there are import issues
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
