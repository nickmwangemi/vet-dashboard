from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth

from .models import VeterinaryOfficer


# Create your views here.


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        vets = VeterinaryOfficer.objects.count()
        active = VeterinaryOfficer.objects.filter(is_active=True).count()
        inactive = VeterinaryOfficer.objects.filter(is_active=False).count()

        context = {
            'vets': vets,
            'active': active,
            'inactive': inactive
        }

        return render(request, 'dashboard/dashboard.html', context)
    else:
        return HttpResponse("You are not allowed to view this resource.")


def onboard_vet(request):
    if not request.user.is_authenticated:
        return HttpResponse("You are not allowed to view this resource.")

    elif request.user.is_authenticated and request.method == "POST":
        form = request.POST
        vet_record_to_save = VeterinaryOfficer()
        vet_record_to_save.name = form['fullname']
        vet_record_to_save.email = form['email']
        vet_record_to_save.county = form['county']
        vet_record_to_save.idNo = form['idNo']
        vet_record_to_save.mobile_number = form['mobile_number']
        vet_record_to_save.save()
        messages.success(request, 'Veterinary Record Saved Successfully')

        return redirect('dashboard:all')

    context = {}
    return render(request, 'dashboard/onboard_vet.html', context)

    # else:
    #     return HttpResponse("You are not allowed to view this resource.")


def vet_records(request):
    if request.user.is_authenticated:
        vets = VeterinaryOfficer.objects.all()
        context = {
            'vets': vets
        }
        return render(request, 'dashboard/vet_records.html', context)

    else:
        return HttpResponse("You are not allowed to view this resource.")


def vet_record_detail(request, pk):
    if not request.user.is_authenticated:
        return HttpResponse("You are not allowed to view this resource.")

    vet_record = VeterinaryOfficer.objects.get(pk=pk)
    if request.user.is_authenticated and request.method == "POST":

        form = request.POST
        vet_record_to_save = vet_record
        vet_record_to_save.name = form['fullname']
        vet_record_to_save.email = form['email']
        vet_record_to_save.county = form['county']
        vet_record_to_save.idNo = form['idNo']
        vet_record_to_save.mobile_number = form['mobile_number']
        is_active = request.POST.getlist('is_active')
        status = bool(is_active)
        vet_record_to_save.is_active = status

        vet_record_to_save.save()
        messages.success(request, 'Veterinary Record Updated Successfully')

    context = {
        'vet_record': vet_record
    }
    return render(request, 'dashboard/vet_record_detail.html', context)
