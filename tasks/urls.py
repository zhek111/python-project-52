from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.TasksView.as_view(), name='list_tasks'),
    path('create/', views.TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(),
         name='update_task'),
    path('<int:pk>/delete/', views.TaskDeleateView.as_view(),
         name='delete_task'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='watch_task')

]
