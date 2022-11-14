
from django.urls import path
from .views import ListView,AddView,UpdateView,DeleteView

urlpatterns = [
    path('list', ListView, name='Task_List'),
    path('add',AddView,name='Add_Task'),
    path('update/<int:task_id>', UpdateView, name='Update_Task'),
    path('delete/<int:task_id>', DeleteView, name='Delete_Task'),
]
