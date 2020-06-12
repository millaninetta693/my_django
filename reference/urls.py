from django.urls import path
from . import views

app_name = 'reference'
urlpatterns = [
    path('', views.reference_list, name='reference_list'),
    path('reference/add/', views.ReferenceCreateView.as_view(), name='reference_create'),
    path('reference/<int:pk>-<slug:slug>/delete/', views.ReferenceDeleteView.as_view(), name='reference_delete'),
    path('reference/<int:pk>-<slug:slug>/update/', views.ReferenceUpdateView.as_view(), name='reference_update'),

]