from django.urls import path
from . import views

app_name = 'bankapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('wikipedia_redirect/<str:district>/', views.wikipedia_redirect, name='wikipedia_redirect'),
    path('application/', views.application_form, name='application_form'),
    path('message/', views.message_page, name='message'),
    path('logout/', views.logout, name='logout'),
]
