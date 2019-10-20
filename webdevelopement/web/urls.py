from django.urls import path
from. import views

urlpatterns = [
    path('',views.home,name='home'),
    path('input',views.input,name='input'),
    path('offer.html',views.fun,name='fun'),
    path('create.html',views.create,name='create'),
    path('home.html',views.home,name='home'),
    path('login.html',views.login,name='login'),
    path('log_data',views.log_data,name='log_data'),
    path('not.html',views.input,name='input'),
    path('check.html',views.check,name='check'),
    path('fer.html',views.fert,name='fer'),
    path('crop.html',views.cr,name='crop'),
]


