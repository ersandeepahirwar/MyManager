from django.shortcuts import render, redirect

from cmsApp.models import (
    Category,
    Discount,
    Product,
    Customer,
    Order,
)

from cmsApp.forms import (
    CategoryForm,
    DiscountForm,
    ProductForm,
    CustomerForm,
    OrderForm,
    SignupForm,
)

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# View created for Dashboard page
@login_required(login_url="login_page")
def DashboardPageView(request):
    total_orders = Order.objects.all().count()
    orders_pending = Order.objects.filter(status="Pending").count()
    orders_delivered = Order.objects.filter(status="Delivered").count()
    orders_out_for_delivery = Order.objects.filter(
        status="Out for Delivery").count()

    context = {
        "total_orders": total_orders,
        "orders_pending": orders_pending,
        "orders_delivered": orders_delivered,
        "orders_out_for_delivery": orders_out_for_delivery,
    }
    return render(request, 'dashboard_page.html', context)


# View created for Categories page
@login_required(login_url="login_page")
def CategoriesPageView(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'categories_page.html', context)


# View created for Add category page
# @login_required(login_url="login_page")
def AddCategoryPageView(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully.")
            return redirect('add_category_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Update category page
@login_required(login_url="login_page")
def UpdateCategoryPageView(request, category_id):
    category = Category.objects.get(id=category_id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category updated successfully.")
            return redirect('categories_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Delete category page
@login_required(login_url="login_page")
def DeleteCategoryPageView(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.error(request, "Category deleted successfully.")
    return redirect('categories_page')


# View created for Discounts page
@login_required(login_url="login_page")
def DiscountsPageView(request):
    discounts = Discount.objects.all()
    context = {
        "discounts": discounts,
    }
    return render(request, 'discounts_page.html', context)


# View created for Add Discount page
@login_required(login_url="login_page")
def AddDiscountPageView(request):
    form = DiscountForm()
    if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Discount added successfully.")
            return redirect('add_discount_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Update Discount page
@login_required(login_url="login_page")
def UpdateDiscountPageView(request, discount_id):
    discount = Discount.objects.get(id=discount_id)
    form = DiscountForm(instance=discount)
    if request.method == 'POST':
        form = DiscountForm(request.POST, instance=discount)
        if form.is_valid():
            form.save()
            messages.success(request, "Discount updated successfully.")
            return redirect('discounts_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Delete Discount page
@login_required(login_url="login_page")
def DeleteDiscountPageView(request, discount_id):
    discount = Discount.objects.get(id=discount_id)
    discount.delete()
    messages.error(request, "Discount deleted successfully.")
    return redirect('discounts_page')


# View created for Products page
@login_required(login_url="login_page")
def ProductsPageView(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, 'products_page.html', context)


# View created for Add Product page
@login_required(login_url="login_page")
def AddProductPageView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully.")
            return redirect('add_product_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Update Product page
@login_required(login_url="login_page")
def UpdateProductPageView(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully.")
            return redirect('products_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Delete Product page
@login_required(login_url="login_page")
def DeleteProductPageView(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.error(request, "Product deleted successfully.")
    return redirect('products_page')


# View created for Customers page
@login_required(login_url="login_page")
def CustomersPageView(request):
    customers = Customer.objects.all()
    context = {
        "customers": customers,
    }
    return render(request, 'customers_page.html', context)


# View created for Add Customer page
@login_required(login_url="login_page")
def AddCustomerPageView(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully.")
            return redirect('add_customer_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Update Customer page
@login_required(login_url="login_page")
def UpdateCustomerPageView(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer updated successfully.")
            return redirect('customers_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Delete Customer page
@login_required(login_url="login_page")
def DeleteCustomerPageView(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    messages.error(request, "Customer deleted successfully.")
    return redirect('customers_page')


# View created for Orders page
@login_required(login_url="login_page")
def OrdersPageView(request):
    orders = Order.objects.all()
    context = {
        "orders": orders,
    }
    return render(request, 'orders_page.html', context)


# View created for Add Order page
@login_required(login_url="login_page")
def AddOrderPageView(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Order added successfully.")
            return redirect('add_order_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Update Order page
@login_required(login_url="login_page")
def UpdateOrderPageView(request, order_id):
    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Order updated successfully.")
            return redirect('orders_page')

    context = {
        "form": form,
    }
    return render(request, 'form.html', context)


# View created for Delete Order page
@login_required(login_url="login_page")
def DeleteOrderPageView(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    messages.error(request, "Order deleted successfully.")
    return redirect('orders_page')


# View created for Signup page
def SignupPageView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                signup_form.save()
                messages.success(request, "Account created successfully.")
                return redirect('signup_page')
            else:
                messages.error(request, "Some error occured!")
                return redirect('signup_page')
        else:
            signup_form = SignupForm()
        context = {'signup_form': signup_form}
        return render(request, 'registration/signup_page.html', context)
    else:
        return redirect('/')


# View created for Login page
def LoginPageView(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have Logged in successfully.")
                return redirect('dashboard_page')
            else:
                messages.error(request, "Invalid Credential!")
                return redirect('login_page')
        return render(request, 'registration/login_page.html')
    else:
        return redirect("/")


# View created for Logout
@login_required(login_url="login_page")
def LogoutView(request):
    logout(request)
    return redirect('login_page')
