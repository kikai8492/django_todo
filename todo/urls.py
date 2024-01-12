
from django.urls import path, include

urlpatterns = [
    path('list/', TodoList.as_view()),
]
