# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Database Tables should be defined as class object
class Customer(models.Model):
    CustomerId          = models.IntegerField(unique=True)
    CustomerName        = models.CharField(max_length=200)

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
    ICS                 = models.CharField(max_length=2)

class SearchDonor(models.Model):

    SearchQuery        = models.CharField(max_length=255)
    
#Maria
class COMP_EDBG(models.Model):
    EDBGEvent_foodID=models.ForeignKey(EDBGFOOD, on_delete=models.CASCADE,primary_key=TRUE)
    FoodEntryID=models.ForeignKey(FOOD, on_delete=models.CASCADE,primary_key=TRUE)
 
class COMP_EMPTYBOWL(models.Model):
    EmptyBowlEvent_foodID=models.ForeignKey(EMPTYBOWLFOOD, on_delete=models.CASCADE,primary_key=TRUE)
    FoodEntryID=models.ForeignKey(FOOD, on_delete=models.CASCADE,primary_key=TRUE)
   
class GENERATE(models.Model):
    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
    reportID=models.ForeignKey(REPORTS, on_delete=models.CASCADE,primary_key=TRUE)
    
class INSTRUCT(models.Model):
    volID=models.ForeignKey(Volunteers, on_delete=models.CASCADE,primary_key=TRUE)
    service_detailID=models.ForeignKey(SERVICEEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
    
class MAINTAIN(models.Model):
    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
    logID=models.ForeignKey(DonationsLog, on_delete=models.CASCADE,primary_key=TRUE)
    
class MAKE_DONATION(models.Model):
    donorID=models.ForeignKey(DONORS, on_delete=models.CASCADE,primary_key=TRUE)
    donationID=models.ForeignKey(DONATIONS, on_delete=models.CASCADE,primary_key=TRUE)
   
class MANAGE_DONATIONS(models.Model):
    donationID=models.ForeignKey(DONATIONS, on_delete=models.CASCADE,primary_key=TRUE)
    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
   
class ORGANIZES(models.Model):
    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
    
class PARTICIPATE_IN(models.Model):
    eventID=models.ForeignKey(FUNDRAISINGEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
    donorID=models.ForeignKey(DONORS, on_delete=models.CASCADE,primary_key=TRUE)

class SERVICE_EVENT_DETAILS(models.Model):
    Service_detailID=models.ForeignKey(SERVICEEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
    Cust_ID=models.ForeignKey(CUSTOMERS, on_delete=models.CASCADE,primary_key=TRUE)
    Review = models.CharField(max_length=100)
    Ratings = models.IntegerField(max_length=20)
    
 class SERVICE_OFFER(models.Model):
    ServiceID=models.ForeignKey(SERVICEEVENTS, on_delete=models.CASCADE,primary_key=TRUE)
    userID=models.ForeignKey(USERS, on_delete=models.CASCADE,primary_key=TRUE)
