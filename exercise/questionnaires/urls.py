from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL mapping to the index view
    path('register/', views.register_user, name='register'),
    path('create/', views.create_questionnaire, name='create_questionnaire'),
    path('login/', views.login, name='login'),
    # Other URL patterns for your app
]
