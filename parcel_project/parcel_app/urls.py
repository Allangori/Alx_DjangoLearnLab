from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/edit/<int:id>/', views.user_edit, name='user_edit'),
    path('users/delete/<int:id>/', views.user_delete, name='user_delete'),
    
    path('parcels/', views.parcel_list, name='parcel_list'),
    path('parcels/create/', views.parcel_create, name='parcel_create'),
    path('parcels/edit/<int:id>/', views.parcel_edit, name='parcel_edit'),
    path('parcels/delete/<int:id>/', views.parcel_delete, name='parcel_delete'),

    path('couriers/', views.courier_list, name='courier_list'),
    path('couriers/create/', views.courier_create, name='courier_create'),
    path('couriers/edit/<int:id>/', views.courier_edit, name='courier_edit'),
    path('couriers/delete/<int:id>/', views.courier_delete, name='courier_delete'),

    path('parcel_tracking/', views.parcel_tracking_list, name='parcel_tracking_list'),
    path('parcel_tracking/create/', views.parcel_tracking_create, name='parcel_tracking_create'),
]
