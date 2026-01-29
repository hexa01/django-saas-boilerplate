from django.urls import path
from .views.home import home, dashboard
from .views.auth import register_view, login_view, logout_view

app_name = 'core'

urlpatterns = [
    path('',home, name ='home'),
    path('register/',register_view, name = 'register'),
    path('dashboard/', dashboard, name = 'dashboard'),
    path('login/',login_view, name = 'login'),
    path('logout/',logout_view, name = 'logout'),
]