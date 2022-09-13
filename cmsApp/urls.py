from django.urls import path

from cmsApp.views import (
    DashboardPageView,

    CategoriesPageView,
    AddCategoryPageView,
    UpdateCategoryPageView,
    DeleteCategoryPageView,

    DiscountsPageView,
    AddDiscountPageView,
    UpdateDiscountPageView,
    DeleteDiscountPageView,

    ProductsPageView,
    AddProductPageView,
    UpdateProductPageView,
    DeleteProductPageView,

    CustomersPageView,
    AddCustomerPageView,
    UpdateCustomerPageView,
    DeleteCustomerPageView,

    OrdersPageView,
    AddOrderPageView,
    UpdateOrderPageView,
    DeleteOrderPageView,

    SignupPageView,
    LoginPageView,
    LogoutView
)


urlpatterns = [
    path('', DashboardPageView, name='dashboard_page'),

    path('categories/', CategoriesPageView, name="categories_page"),
    path('add_category', AddCategoryPageView, name="add_category_page"),
    path('update_category/<str:category_id>',
         UpdateCategoryPageView, name="update_category_page"),
    path('delete_category/<str:category_id>',
         DeleteCategoryPageView, name="delete_category_page"),

    path('discounts/', DiscountsPageView, name="discounts_page"),
    path('add_discount', AddDiscountPageView, name="add_discount_page"),
    path('update_discount/<str:discount_id>',
         UpdateDiscountPageView, name="update_discount_page"),
    path('delete_discount/<str:discount_id>',
         DeleteDiscountPageView, name="delete_discount_page"),

    path('products/', ProductsPageView, name="products_page"),
    path('add_product', AddProductPageView, name="add_product_page"),
    path('update_product/<str:product_id>',
         UpdateProductPageView, name="update_product_page"),
    path('delete_product/<str:product_id>',
         DeleteProductPageView, name="delete_product_page"),

    path('customers/', CustomersPageView, name="customers_page"),
    path('add_customer', AddCustomerPageView, name="add_customer_page"),
    path('update_customer/<str:customer_id>',
         UpdateCustomerPageView, name="update_customer_page"),
    path('delete_customer/<str:customer_id>',
         DeleteCustomerPageView, name="delete_customer_page"),

    path('orders/', OrdersPageView, name="orders_page"),
    path('add_order', AddOrderPageView, name="add_order_page"),
    path('update_order/<str:order_id>',
         UpdateOrderPageView, name="update_order_page"),
    path('delete_order/<str:order_id>',
         DeleteOrderPageView, name="delete_order_page"),

    path('signup', SignupPageView, name='signup_page'),
    path('login', LoginPageView, name='login_page'),
    path('logout', LogoutView, name='logout'),

]
