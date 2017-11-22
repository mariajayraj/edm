# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Database Tables should be defined as class object
class Customer(models.Model):
    CustomerId          = models.IntegerField(max_length=20,primary_key=True)
    CustomerFirstName   = models.CharField(max_length=200)
    CustomerLastName    = models.CharField(max_length=200)
    Street= models.CharField(max_length=200)
    City= models.CharField(max_length=200)
    State= models.CharField(max_length=200)
    Zip=models.IntegerField(max_length=10)

class Donors(models.Model):
    OrganizationName    = models.CharField(max_length=100)
    Salutation          = models.CharField(max_length=100)
    FirstName           = models.CharField(max_length=100)
    LastName            = models.CharField(max_length=100)
    Email               = models.EmailField(max_length=100)
    PhoneNumber         = models.CharField(max_length=15)
    Comments            = models.CharField(max_length=100)
    StreetAddress       = models.CharField(max_length=100)
    City                = models.CharField(max_length=100)
    State               = models.CharField(max_length=100)
    Zip                 = models.CharField(max_length=100)
    isPurchased_by_ICS  = models.BooleanField(default=False)
  
class DonationsLog(models.Model):
    logID= models.IntegerField(max_length=20,primary_key=True)
    lastModifidDate=models.DateField()
    lastChangedBy=models.CharField(max_length=100)


class SearchDonor(models.Model):
    donorID =models.IntegerField(max_length=20,primary_key=True)
    SearchQuery= models.CharField(max_length=255)

class Donations(models.Model):
    donationID =models.IntegerField(max_length=20,primary_key=True)
    donation_date=models.DateField()
    additional_comments=models.CharField(max_length=100)

class EBDGFOOD(models.Model):
    EDBGEvent_foodID= models.IntegerField(max_length=20,primary_key=True)
    ServingsPerGallon=models.IntegerField(max_length=20)
    EBDGtype=models.CharField(max_length=20)
    RestaurantName=models.CharField(max_length=100)
    
class EBDGRAFFLE(models.Model):
    eventID=models.IntegerField(max_length=20,primary_key=True)
    donation=models.CharField(max_length=100)

class EMPTYBOWLRAFFLEAUCTION(models.Model):
    eventID=models.IntegerField(max_length=20,primary_key=True)
    description=models.CharField(max_length=100)
    item=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    receivedDate=models.DateField()
 
class EMPTYBOWLFOOD(models.Model):
    EmptyBowlEvent_foodID=models.IntegerField(max_length=20,primary_key=True)
    food_description=models.CharField(max_length=100)
    quantity=models.IntegerField(max_length=20)
    totalServings=models.IntegerField(max_length=20)
    
class FOOD(models.Model): 
    foodEntryID=models.IntegerField(max_length=20,primary_key=True)
    foodtype=models.CharField(max_length=100)
    avgCost=models.IntegerField(max_length=20)
    totalPounds=models.IntegerField(max_length=20)
    totalValue=models.IntegerField(max_length=20)
 
class FOODCATEGORY(models.Model):
    donationID=models.IntegerField(max_length=20,primary_key=True)
    categoryID=models.IntegerField(max_length=20)
    
class FOODENTRY(models.Model):
    CategoryID=models.IntegerField(max_length=20)
    foodEntryID=models.IntegerField(max_length=20,primary_key=True)
    
class FOODCATEGORYDESC(models.Model):
    categoryID=models.IntegerField(max_length=20)
    description=models.CharField(max_length=100)
    categoryName=models.CharField(max_length=100)
 
class FUNDRAISING_EVENTS(models.Model):
eventID=models.IntegerField(max_length=20,primary_key=True)
estimatedValue=models.IntegerField(max_length=20)
receivedDate=models.DateField()
location=models.CharField(max_length=100)

class GOLF(models.Model):
    eventID=models.IntegerField(max_length=20,primary_key=True)
    dtype=models.CharField(max_length=100)
    
class ITEMS(models.Model):
    donationID=models.IntegerField(max_length=20,primary_key=True)
    description=models.CharField(max_length=100)
    isack_sent=models.BooleanField(default=False)
    approxValue=models.IntegerField(max_length=20)
 
class MONETARY (models.Model):
    donationID=models.IntegerField(max_length=20,primary_key=True)
    amount=models.IntegerField(max_length=20)
    modeOfPayment=models.CharField(max_length=100)
 
class Reports(models.Model):
    reportID=models.IntegerField(max_length=20,primary_key=True)
    filename=models.CharField(max_length=100)
    reportgen_date=models.DateField()
    
 class ServiceEvents(models.model)
service_detailID=models.IntegerField(max_length=20,primary_key=True)
date_of_service=models.DateField()
serviceID=models.IntegerField(max_length=20)
