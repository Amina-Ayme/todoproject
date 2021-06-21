from django.urls import path
from . views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, CustomRegister

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', CustomRegister.as_view(), name="register"),
    path('', TaskList.as_view(), name="maintask"),
    path('task/<str:pk>/', TaskDetail.as_view(), name="detail"),
    path('create-task/', TaskCreate.as_view(), name="create_task"),
    path('update-task/<str:pk>/', TaskUpdate.as_view(), name="update_task"),
    path('delete_task/<str:pk>/', TaskDelete.as_view(), name="delete_task"),
]
