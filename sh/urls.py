from django.urls import path
from . import views

app_name = 'sh'
urlpatterns = [
    path('', views.index, name='index'),
    path('shop', views.add , name='add'),
    path('expense', views.expenses, name='expense'),
]