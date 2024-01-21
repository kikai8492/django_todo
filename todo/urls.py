
from django.urls import path, include
from .views import TodoList
from .views import TodoDetail
from .views import TodoCreate
from .views import TodoDelete

urlpatterns = [
  path('list/', TodoList.as_view(), name='list'),
  path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
  path('create/', TodoCreate.as_view(), name='create'),
  path('delete/<int:pk>',TodoDelete.as_view(), name='delete'),
]
