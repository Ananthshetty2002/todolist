from django.urls import path
from . import views
from .views import toggle_task,task_create,task_list,category_create



urlpatterns=[
     path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:pk>', views.task_update, name='task_update'),
    path('delete/<int:pk>', views.task_delete, name='task_delete'),
    path('category',category_create, name='category_create'),
    path('login',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
     path('toggle_task/<int:task_id>', toggle_task, name='toggle_task'),
     path("categories/",views.category_list, name="category_list"),
     path('delete<int:task_id>',views.delete, name='delete'),
]