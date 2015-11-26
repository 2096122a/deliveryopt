from django.db import models
from django.template.defaultfilters import slugify
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    driver = models.BooleanField(default=False)
    VehicleHeight = models.IntegerField(default=0)
    VehicleLength = models.IntegerField(default=0)
    VehicleWidth = models.IntegerField(default=0)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class PostedItem(models.Model):
    itemName = models.CharField(max_length=128, default="")
    SenderName = models.CharField(max_length=128, default="")
    pickUpAddress1 = models.CharField(max_length=128, default="")
    pickUpPostCode = models.CharField(max_length=128, default="")
    pickUpContactNumber = models.IntegerField(default=0)
    RecipientName = models.CharField(max_length=128, default="")
    dropOffAddress1 = models.CharField(max_length=128, default="")
    dropOffPostCode = models.CharField(max_length=128, default="")
    dropOffContactNumber = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    complete = models.CharField(max_length=20, default="pending")
    mslug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.itemName)
                super(PostedItem, self).save(*args, **kwargs)
    

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.itemName

class Route(models.Model):
    driverName = models.CharField(max_length=128, default="")
    end = models.CharField(max_length=128, default="")
    start = models.CharField(max_length=128, default="")
    via = models.CharField(max_length=128, null=True, default="")
    date = models.DateField(default=date.today)
    rslug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
                self.slug = slugify(self.driverName)
                super(Route, self).save(*args, **kwargs)


    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.driverName
