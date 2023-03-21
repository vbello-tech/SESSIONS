from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse
from business.models import Business


class BookedSession(models.Model):
    class Type(models.TextChoices):
        RENTED = 'rented', 'Rented',
        SOLD = 'sold', 'Sold',
        AVAILABLE = 'available', 'Available'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="business_admin", blank=True, null=True, on_delete=models.CASCADE)
    day = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    type = models.CharField(max_length=9, choices=Type.choices)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True)
    opened = models.BooleanField(default=False, blank=True, null=True)
    user_closed = models.BooleanField(default=False, blank=True, null=True)
    admin_closed = models.BooleanField(default=False, blank=True, null=True)
    active = models.BooleanField(default=False, blank=True, null=True)
    ref_code = models.SlugField(blank=True, null=True, unique=True)
    opened_date = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False, blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)  # date business was registered

    def user_close_func(self):
        if self.admin_closed:
            self.closed=True
            self.closed_date=timezone.now()

    def admin_close_func(self):
        if self.user_closed:
            self.closed = True
            self.closed_date = timezone.now()