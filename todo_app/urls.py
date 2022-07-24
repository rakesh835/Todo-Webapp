from django.urls import path, include

from . import views 




urlpatterns = [
    path('', views.home, name="todo-home"),
    path('del/<int:item_id>', views.delete, name="todo-delete"),
    path('update/<int:item_id>', views.update, name="todo-update"),
]