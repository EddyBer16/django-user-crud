from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.usersIndex, name='index'),
    path('<int:id>', views.getUser, name='getById'),
]