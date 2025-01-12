
from django.contrib import admin
from .models import Admin, User, Parcel, Courier, ParcelTracking

admin.site.register(Admin)
admin.site.register(User)
admin.site.register(Parcel)
admin.site.register(Courier)
admin.site.register(ParcelTracking)
