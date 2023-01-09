from django.contrib import admin
from django.urls import path, include
from task_manager import views
from task_manager.views import LoginUserView, LogoutUserView

urlpatterns = [
    path('a/', views.index),
    path('', views.IndexView.as_view()),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('users/', include('users.urls')),
    path('statuses/', include('statuses.urls')),
    path('tasks/', include('tasks.urls')),
    path('labels/', include('labels.urls')),
    path('admin/', admin.site.urls)
]
