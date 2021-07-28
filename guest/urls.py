from django.urls import path

from .views import AddGuestView, AllGuestView, GuestHistoryView, SignOutGuestView

urlpatterns = [
    path('', AllGuestView, name='all-guests'),
    path('add-guest/', AddGuestView, name='add-guest'),
    path('guest-history/', GuestHistoryView, name='guest-history'),
    path('signout-guest/<int:pk>/', SignOutGuestView, name='signout-guest')
]

