from django.urls import path
from . import views 

urlpatterns = [
    path("",views.base,name="base"),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
]
