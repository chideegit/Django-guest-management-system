from guest.models import GuestTable
from django.shortcuts import render, redirect

from .form import AddGuestForm

def AddGuestView(request):
    if request.method == 'POST':
        form = AddGuestForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('all-guests')
    else:
        form = AddGuestForm()
    context = {'form':form}
    return render(request, 'guest/add_guest.html', context)

def SignOutGuestView(request, pk):
    obj = GuestTable.objects.get(id=pk)
    obj.signed_out = False
    obj.save()
    return redirect('all-guest')

def AllGuestView(request):
    obj = GuestTable.objects.filter(signed_out = True)
    context = {'obj':obj}
    return render(request, 'guest/all_guests.html', context)

def GuestHistoryView(request):
    obj = GuestTable.objects.all()
    context = {'obj':obj}
    return render(request, 'guest/guest_history.html', context)