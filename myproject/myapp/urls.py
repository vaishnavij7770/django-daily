from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('contact', views.contact),
    # path('register', views.register),
    # path('formsave',views.formsave),
    path('registration',views.registration),
    path('saveform',views.saveform),
    path('viewdata',views.viewdata),
]