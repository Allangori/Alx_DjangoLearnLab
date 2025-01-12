from django import forms
from .models import User, Parcel, Courier, ParcelTracking

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'phone_number', 'address']

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['user', 'description', 'source_location', 'destination_location', 'current_status', 'weight']

class CourierForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = ['full_name', 'phone_number', 'assigned_city', 'email', 'status']

class ParcelTrackingForm(forms.ModelForm):
    class Meta:
        model = ParcelTracking
        fields = ['parcel', 'courier', 'status_update']
