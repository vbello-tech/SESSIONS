from django.db import models
from django.conf import settings
import random, string
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from location_field.models.plain import PlainLocationField


# Create your models here.

#generate random 5 digits that would be used as business code.
def code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

CATEGORY_CHOICES = (
    ('DRY CLEANING', 'DRY CLEANING'),
    ('SALON', 'SALON'),
    ('CARPENTARY AND WOOD WORK', 'CARPENTARY AND WOOD WORK')
)

# Model for Business Details and Properties
class Business(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#business owner
    name = models.CharField(max_length=300)#business name
    image = models.ImageField(blank=True, upload_to="Business/")#image of business
    description = models.CharField(max_length=60, blank=True, null=True)
    category = models.CharField(max_length=200, blank =False, null=False,)#category business falls under
    active = models.BooleanField(default="True")#only business with active == true can have a scheduled session
    sessions_completed = models.IntegerField(default=0, blank=True, null=True)#number of sessions completed
    created_date = models.DateTimeField(auto_now_add=True)#date business was registered
    banned_date = models.DateTimeField(blank=True, null=True)#date business active status was changed to false
    phone = PhoneNumberField(blank=True, null=True)
    city = models.CharField(max_length=255)#business city
    location = PlainLocationField(blank=True, null=True, based_fields=['city'], zoom=7)
    address = models.CharField(max_length=100, blank=True, null=True)#business address
    code = models.SlugField(blank=True, null=True, unique=True)#unique business code for each business

    class Meta:
        ordering = ['-created_date']
        verbose_name = _("Business")

    def __str__(self):
        return self.name