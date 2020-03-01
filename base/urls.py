from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index_page, name='index'),
    path('security/', security_page, name='security'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
]