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


class SearchDonor(models.Model):
    donorID =models.IntegerField(max_length=20,primary_key=True)
    SearchQuery        = models.CharField(max_length=255)

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
    eventID
    description 
    item 
    status
    receivedDate
 
class EMPTYBOWLFOOD(models.Model):
    EmptyBowlEvent_foodID
    food_description
    quantity
    totalServings
    
class FOOD(models.Model): 
    foodEntryID
    foodtype
    avgCost
    totalPounds
    totalValue
 
class FOODCATEGORY(models.Model):
    donationID
    categoryID
    
class FOODENTRY(models.Model):
    CategoryID
    foodEntryID  
    
class FOODCATEGORYDESC(models.Model):
    categoryID
    description
    categoryName
 
class FUNDRAISING_EVENTS(models.Model):
eventID
estimatedValue
receivedDate
location

class GOLF(models.Model):
    eventID
    dtype
    
class ITEMS(models.Model):
    donationID
    description
    isack_sent
    approxValue
 
class MONETARY (models.Model):
    donationID
    amount
    modeOfPayment
 
class Reports(models.Model):
    reportID
    filename
    reportgen_date
    
  
