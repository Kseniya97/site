from  django.conf.urls import url, include
from  django.contrib import  admin
from . import  views
urlpatterns =[
    url(r'^$', views.price, name='price'),
url(r'^paric/', views.paric, name='paric'),
url(r'^nogty/', views.nogty, name='nogty'),
url (r'^other/', views.other, name='other'),
]