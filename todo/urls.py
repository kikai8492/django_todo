
from django.urls import path, include
from .views import TodoList
from .views import TodoDetail
from .views import TodoCreate

urlpatterns = [
  path('list/', TodoList.as_view()),
  path('detail/<int:pk>', TodoDetail.as_view()),
  path('create/', TodoCreate.as_view()),
]
