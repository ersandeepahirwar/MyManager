from django.db import models


# Model created for Category
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=235, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '1. Categories of Products'

    def __str__(self):
        return self.title


# Model created for Discount
class Discount(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=235, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '2. Discounts on Products'

    def __str__(self):
        return self.title


# Model created for Product
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=235, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "3. Total Products"

    def __str__(self):
        return self.title


# Model created for Customer
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=235, null=True)
    email = models.EmailField(max_length=235, null=True)
    phone = models.CharField(max_length=235, null=True)
    address = models.CharField(max_length=235, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "4. Total Customers"

    def __str__(self):
        return self.name


# Model created for Order
class Order(models.Model):
    status_choices = (
        ("Pending", "Pending"),
        ("Delivered", "Delivered"),
        ("Out for Delivery", "Out for Delivery"),
    )
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=235, choices=status_choices)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "5. Total Orders"

    def __str__(self):
        return f"Order of {self.customer.name} | Status - {self.status}"
