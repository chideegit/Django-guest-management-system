from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .form import AddGuestForm
from .models import GuestTable

@login_required
def AddGuestView(request):
    if request.method == 'POST':
        form = AddGuestForm(request.POST)
        if form.is_valid:
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            return redirect('all-guests')
    else:
        form = AddGuestForm()
    context = {'form':form}
    return render(request, 'guest/add_guest.html', context)

@login_required
def SignOutGuestView(request, pk):
    obj = GuestTable.objects.get(id=pk)
    obj.signed_out = True
    obj.save()
    return redirect('all-guests')

@login_required
def AllGuestView(request):
    obj = GuestTable.objects.all().order_by('-time_in')[:10]
    context = {'obj':obj}
    return render(request, 'guest/all_guests.html', context)

@login_required
def GuestHistoryView(request):
    obj = GuestTable.objects.all().order_by('-time_in')
    context = {'obj':obj}
    return render(request, 'guest/guest_history.html', context)