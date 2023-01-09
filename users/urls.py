from django.urls import path
from users import views

urlpatterns = [
    path('', views.UsersView.as_view(), name='list_users'),
    path('create/', views.UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/update/', views.UserUpdateView.as_view(),
         name='update_user'),
    path('<int:pk>/delete/', views.UserDeleateView.as_view(),
         name='delete_user')
]
