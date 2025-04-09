from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('EVIRATA', views.EVIRATA, name='EVIRATA'),
    path('FRONX', views.FRONX, name='FRONX'),
    path('INVICTO', views.INVICTO, name='INVICTO'),
    path('JIMNY', views.JIMNY, name='JIMNY'),
    path('CIAZ', views.CIAZ, name='CIAZ'),
    path('BALENO', views.BALENO, name='BALENO'),
    path('GRAND_VIRATA', views.GRAND_VIRATA, name='GRAND_VIRATA'),
    path('IGNIS', views.IGNIS, name='IGNIS'),
    path('XL6', views.XL6, name='XL6'),
    path('inquiry/', views.person_form, name='person_form'),
    path('success/', views.success, name='success'), 
]