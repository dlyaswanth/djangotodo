
from django.urls import path
from .views import AddUser, Login,Logout
urlpatterns = [
    path('create', AddUser, name='CreateUser'),
    path('login', Login, name='LoginUser'),
    path('logout', Logout, name='LogoutUser'),
]
