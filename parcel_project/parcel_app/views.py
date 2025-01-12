from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import User, Parcel, Courier, ParcelTracking
from .forms import UserForm, ParcelForm, CourierForm, ParcelTrackingForm



def home(request):
    return render(request, 'home.html')
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('user_list') 
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})

def user_edit(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_edit.html', {'form': form})

def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_delete.html', {'user': user})


def parcel_list(request):
    parcels = Parcel.objects.all()
    return render(request, 'parcel_list.html', {'parcels': parcels})

def parcel_create(request):
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parcel_list')
    else:
        form = ParcelForm()
    return render(request, 'parcel_create.html', {'form': form})

def parcel_edit(request, id):
    parcel = get_object_or_404(Parcel, id=id) 
    if request.method == 'POST':
        form = ParcelForm(request.POST, instance=parcel)
        if form.is_valid():
            form.save()
            return redirect('parcel_list')
    else:
        form = ParcelForm(instance=parcel)
    return render(request, 'parcel_edit.html', {'form': form})

def parcel_delete(request, id):
    parcel = get_object_or_404(Parcel, id=id)
    if request.method == 'POST':
        parcel.delete()
        return redirect('parcel_list')
    return render(request, 'parcel_delete.html', {'parcel': parcel})


def courier_list(request):
    couriers = Courier.objects.all()
    return render(request, 'courier_list.html', {'couriers': couriers})

def courier_create(request):
    if request.method == 'POST':
        form = CourierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courier_list')
    else:
        form = CourierForm()
    return render(request, 'courier_create.html', {'form': form})

def courier_edit(request, id):
    courier = get_object_or_404(Courier, id=id)
    if request.method == 'POST':
        form = CourierForm(request.POST, instance=courier)
        if form.is_valid():
            form.save()
            return redirect('courier_list')
    else:
        form = CourierForm(instance=courier)
    return render(request, 'courier_edit.html', {'form': form})

def courier_delete(request, id):
    courier = get_object_or_404(Courier, id=id)
    if request.method == 'POST':
        courier.delete()
        return redirect('courier_list')
    return render(request, 'courier_delete.html', {'courier': courier})


def parcel_tracking_list(request):
    parcel_trackings = ParcelTracking.objects.all()
    return render(request, 'parcel_tracking_list.html', {'parcel_trackings': parcel_trackings})

def parcel_tracking_create(request):
    if request.method == 'POST':
        form = ParcelTrackingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parcel_tracking_list')
    else:
        form = ParcelTrackingForm()
    return render(request, 'parcel_tracking_create.html', {'form': form})



def user_list(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)

def parcel_list(request):
    parcels = list(Parcel.objects.values())
    return JsonResponse(parcels, safe=False)

def courier_list(request):
    couriers = list(Courier.objects.values())
    return JsonResponse(couriers, safe=False)

def courier_detail(request, courier_id):
    courier = get_object_or_404(Courier, pk=courier_id)
    courier_data = {
        "id": courier.id,
        "full_name": courier.full_name,
        "phone_number": courier.phone_number,
        "assigned_city": courier.assigned_city,
        "email": courier.email,
        "status": courier.status,
        "created_at": courier.created_at,
    }
    return JsonResponse(courier_data)


@method_decorator(csrf_exempt, name='dispatch')
def update_courier_status(request, courier_id):
    if request.method == 'PUT':
        courier = get_object_or_404(Courier, pk=courier_id)
        try:
            data = json.loads(request.body)
            new_status = data.get('status', None)

            if new_status in ['Available', 'On Delivery']:
                courier.status = new_status
                courier.save()
                return JsonResponse({"message": "Courier status updated successfully."})
            else:
                return JsonResponse({"error": "Invalid status value."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
    return JsonResponse({"error": "Invalid request method. Use PUT."}, status=405)


def tracking_list(request):
    trackings = list(ParcelTracking.objects.values())
    return JsonResponse(trackings, safe=False)


def parcel_tracking_detail(request, parcel_id):
    trackings = ParcelTracking.objects.filter(parcel_id=parcel_id).values()
    if trackings.exists():
        return JsonResponse(list(trackings), safe=False)
    else:
        return JsonResponse({"error": "No tracking records found for this parcel."}, status=404)


@method_decorator(csrf_exempt, name='dispatch')
def add_tracking_update(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            parcel_id = data.get('parcel_id')
            courier_id = data.get('courier_id')
            status_update = data.get('status_update')

            if not (parcel_id and courier_id and status_update):
                return JsonResponse({"error": "All fields are required."}, status=400)

            parcel = get_object_or_404(Parcel, pk=parcel_id)
            courier = get_object_or_404(Courier, pk=courier_id)

            tracking = ParcelTracking.objects.create(
                parcel=parcel,
                courier=courier,
                status_update=status_update
            )
            return JsonResponse({"message": "Tracking update added successfully.", "tracking_id": tracking.id})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
    return JsonResponse({"error": "Invalid request method. Use POST."}, status=405)



