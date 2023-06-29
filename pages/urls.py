from django.urls import path
from . import views 

urlpatterns = [
    path("",views.base,name="base"),
    path("index",views.index,name="index"),
    path('contact',views.contact,name='contact'),
    path('offer',views.offer,name='offer'),
]
