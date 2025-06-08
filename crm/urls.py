from django.urls import path
from . import views

app_name = 'crm'

urlpatterns = [
    # Клиенты
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    # Сделки
    path('clients/<int:client_id>/deals/', views.client_deals, name='client_deals'),
    path('clients/<int:client_id>/deals/create/', views.deal_create, name='deal_create'),
    path('deals/<int:pk>/edit/', views.deal_edit, name='deal_edit'),
    path('deals/<int:pk>/delete/', views.deal_delete, name='deal_delete'),
]