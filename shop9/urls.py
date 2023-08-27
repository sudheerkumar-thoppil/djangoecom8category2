from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category<int:category>/', views.category ,name='category'),
    path('cats/',views.cats,name='cats'),
    path('register/',views.register,name='register'),

   
]