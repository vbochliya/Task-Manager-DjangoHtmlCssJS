
from django.urls import path
from task.views import *

urlpatterns = [
    path('',index,name='home'),
    path('new-task/',new_task,name='new_task'),
    path('completed-tasks/',completed_tasks,name='completed_tasks'),
    path('pending-tasks/',pending_tasks,name='pending_tasks'),
    path('todays-tasks/',todays_tasks,name='todays_tasks'),
    path('complete-the-task/',complete_the_task,name='complete_the_task'),
    path('delete-the-task/',delete_the_task,name='delete_the_task'),
    
]