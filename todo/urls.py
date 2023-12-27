from django.urls import path
from .views import TodoListApi, TodoDetailApi, TodoCreateApi, TodoDeleteApi, TodoListCompletedApi

urlpatterns = [
    path('current/', TodoListApi.as_view()),
    path('completed/', TodoListCompletedApi.as_view()),
    path('<int:pk>/', TodoDetailApi.as_view()),
    path('create/', TodoCreateApi.as_view()),
    path('delete/<int:pk>/', TodoDeleteApi.as_view())
]