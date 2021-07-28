from django.db import models
from django.contrib.auth.models import User

class GuestTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guest_names = models.CharField(max_length=100)
    guest_email = models.EmailField(max_length=100, null=True, blank=True)
    guest_no = models.CharField('Guest Phone Number', max_length=20, null=True, blank=True)
    to_see = models.CharField(max_length=100)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(auto_now=True)
    signed_out = models.BooleanField(default=False)
    