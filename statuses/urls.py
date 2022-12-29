from django.urls import path

from statuses import views


urlpatterns = [
    path('', views.StatusView.as_view(), name='list_statuses'),
    path('create/', views.StatusCreateView.as_view(), name='create_status'),
    path('<int:pk>/update/', views.StatusUpdateView.as_view(), name='update_status'),
    path('<int:pk>/delete/', views.StatusDeleateView.as_view(), name='delete_status')
]