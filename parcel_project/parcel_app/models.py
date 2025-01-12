from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Parcel(models.Model):
    PENDING = 'Pending'
    IN_TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (IN_TRANSIT, 'In Transit'),
        (DELIVERED, 'Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    source_location = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=100)
    current_status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PENDING
    )
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Parcel {self.parcel_id} - {self.description}"

class Courier(models.Model):
    AVAILABLE = 'Available'
    ON_DELIVERY = 'On Delivery'
    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (ON_DELIVERY, 'On Delivery'),
    ]
    
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    assigned_city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=AVAILABLE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class ParcelTracking(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    status_update = models.CharField(max_length=255)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tracking {self.tracking_id} - {self.status_update}"
