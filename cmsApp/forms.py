from cmsApp.models import (
    Category,
    Discount,
    Product,
    Customer,
    Order,
)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Form created for Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex- Sports"})
        }
        labels = {
            'title': 'Category',
        }


# Form created for Discount
class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex- 20%"})
        }
        labels = {
            'title': 'Discount',
        }


# Form created for Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex - Cricket Bat"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control", "placeholder": "Ex- 999"}),
            "discount": forms.Select(attrs={"class": "form-control"}),
        }
        labels = {
            'title': 'Product',
            'category': 'Category',
            'price': 'Price',
            'discount': 'Discount',
        }


# Form created for Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "John Doe"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "johndoe@gmail.com"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tel +9114000032"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "NH-10, Jhansi, India"}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'address': 'Address',
        }


# Form created for Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            "customer": forms.Select(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),

        }
        labels = {
            'customer': 'Customer',
            'product': 'Product',
            'status': 'Status',
        }


# Form created for Signup Page
class SignupForm(UserCreationForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "John",
        }),
        label="First name"
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "Doe",
        }),
        label="Last name"
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "text",
            "placeholder": "johndoe",
        }),
        label="Username"
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "type": "email",
            "placeholder": "johndoe@gmail.com",
        }),
        label="Email"
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "type": "password",
        }),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "type": "password",
        }),
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]
