from django import forms
from django.db.models import fields

from .models import GuestTable

class AddGuestForm(forms.ModelForm):
    class Meta:
        model = GuestTable
        exclude = ('user', 'time_in', 'time_out', 'signed_out', )
