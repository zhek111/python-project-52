from django.contrib import admin
from django.urls import path, include

from task_manager import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls)
]
