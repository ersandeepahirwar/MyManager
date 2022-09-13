from django.contrib import admin

from cmsApp.models import (
    Category,
    Discount,
    Product,
    Customer,
    Order,
)


# Model created for Category for Admin Panel
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created"]


# Model created for Discount for Admin Panel
class DiscountAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created"]


# Model created for Product for Admin Panel
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "price", "discount", "date_created"]


# Model created for Customer for Admin Panel
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address", "date_created"]


# Model created for Order for Admin Panel
class OrderAdmin(admin.ModelAdmin):
    list_display = ["customer", "product", "status", "date_created"]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
