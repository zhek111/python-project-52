from django.urls import path
from labels import views

urlpatterns = [
    path('', views.LabelsView.as_view(), name='list_labels'),
    path('create/', views.LabelsCreateView.as_view(), name='create_label'),
    path('<int:pk>/update/', views.LabelsUpdateView.as_view(),
         name='update_label'),
    path('<int:pk>/delete/', views.LabelsDeleateView.as_view(),
         name='delete_label')
]
