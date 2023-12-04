from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL mapping to the index view
    path('register/', views.register_user, name='register'),
    path('create/', views.create_questionnaire, name='create_questionnaire'),
    path('customer-login/', views.customer_login, name='customer_login'),
    path('admin-login/', views.admin_login, name='admin_login'),
    # Other URL patterns for your app
    path('list_customers/', views.list_customers, name='list_customers'),
    path('customer/<int:customer_id>/', views.customer_responses, name='customer_responses'),
    path('create_questionnaire/', views.create_questionnaire, name='create_questionnaire'),
    # Other URL patterns as needed
]
