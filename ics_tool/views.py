# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.template import Context
import datetime
from django.http import HttpResponse
import re

from .forms import *
from .models import *


def health(request):
    return HttpResponse("3")

#@login_required(login_url="login/")
def index(request):
    template_name = 'ics_tool/home.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDataForm(request.POST)
    if form.is_valid():

      results = 'Welcome'

      return render(request,'ics_tool/home.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/home.html',{})

def add_donor(request):
    template_name = 'ics_tool/add_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = AddDonorForm(request.POST)
    if form.is_valid():
      OrganizationName = request.POST.get('OrganizationName', '')
      Salutation       = request.POST.get('Salutation', '')
      FirstName        = request.POST.get('FirstName', '')
      LastName         = request.POST.get('LastName', '')
      Email            = request.POST.get('Email', '')
      PhoneNumber      = request.POST.get('PhoneNumber', '')
      Comments         = request.POST.get('Comments', '')
      StreetAddress    = request.POST.get('StreetAddress', '')
      City             = request.POST.get('City', '')
      State            = request.POST.get('State', '')
      Zip              = request.POST.get('Zip', '')
      ICS              = request.POST.get('ICS', '')

      LoadDonorObj = Donors(OrganizationName=OrganizationName,Salutation=Salutation,FirstName=FirstName,LastName=LastName,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,ICS=ICS)
      LoadDonorObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/add_donor.html',{})

def search_donor(request):

    template_name = 'ics_tool/search_donor.html'

    if request.method == "GET":
        return render(request, template_name)

    form = SearchDonorForm(request.POST)
    if form.is_valid():
      SearchQuery = request.POST.get('SearchQuery', '')

      results = Donors.objects.filter(Q(FirstName__icontains=SearchQuery)).values()

      return render(request,'ics_tool/donor_results.html',{'Results' : results})

    print(form.errors)

    return render(request,'ics_tool/search_donor.html',{})


def add_golf(request):
    template_name = 'ics_tool/Golf_Add_donations.html'

    if request.method == "GET":
        return render(request, template_name)

    form = GolfAddDonationsform(request.POST)
    if form.is_valid():
       CompanyName          = request.POST.get('CompanyName', '')
       Title                = request.POST.get('Title ', '')
       DonorContactPerson   = request.POST.get('DonorContactPerson ', '')
       StreetAddress        = request.POST.get('StreetAddress', '')
       City                 = request.POST.get('City', '')
       State                = request.POST.get('State', '')
       Zip                  = request.POST.get('Zip', '')
       PhoneNumber          = request.POST.get('PhoneNumber', '')
       Email                = request.POST.get('Email', '')
       DoantionDescription  = request.POST.get('DoantionDescription', '')
        EstimateValue       = request.POST.get('EstimateValue', '')
        UserContactPerson   = request.POST.get('UserContactPerson', '')
        ReceivedDate        = request.POST.get('ReceivedDate ', '')
        DonationType        = request.POST.get('DonationType', '')
        Comments            = request.POST.get('Comments', '')
    
      LoadGolfObj = GOLF(CompanyName=CompanyName,Title=Title, DonorContactPerson= DonorContactPerson,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,
                         DoantionDescription=DoantionDescription,  EstimateValue=EstimateValue ,UserContactPerson=UserContactPerson,
                          ReceivedDate=ReceivedDate, DonationType=DonationType )
      LoadGolfObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/Golf_Add_donations.html',{})

def add_EDBGRaffle(request):
    template_name = 'ics_tool/EDBG_Raffle_Donations.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EDBGRaffleDonationsform(request.POST)
    if form.is_valid():
       DonorCompanyName     = request.POST.get('DonorCompanyName', '')
       Title                = request.POST.get('Title ', '')
       StreetAddress        = request.POST.get('StreetAddress', '')
       City                 = request.POST.get('City', '')
       State                = request.POST.get('State', '')
       Zip                  = request.POST.get('Zip', '')
       PhoneNumber          = request.POST.get('PhoneNumber', '')
       Email                = request.POST.get('Email', '')
       DoantionDescription  = request.POST.get('DoantionDescription', '')
    EstimateValue           = request.POST.get('EstimateValue', '')
    ReceivedDate            = request.POST.get('ReceivedDate ', '')
      Comments              = request.POST.get('Comments', '')
    
      LoadEDBGRaffObj = EBDGRAFFLE(DonorCompanyName=DonorCompanyName,Title=Title, 
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,
                         DoantionDescription=DoantionDescription,  EstimateValue=EstimateValue ,
                          ReceivedDate=ReceivedDate )
      LoadEDBGRaffObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/EDBG_Raffle_Donations.html',{})


def add_EDBGFood(request):
    template_name = 'ics_tool/EDBG_Food_Donations.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EDBGFoodDonationsform(request.POST)
    if form.is_valid():
    EDBGDonorCompanyName    = request.POST.get('EDBGDonorCompanyName', '')
    DonorType               = request.POST.get(' DonorType ', '')
    FoodType                = request.POST.get('FoodType', '')
    ServingsperGallon       = request.POST.get('ServingsperGallon', '')
    AverageCostperServing   = request.POST.get('AverageCostperServing', '')
    TotalValue              = request.POST.get('TotalValue ', '')
    Comments                = request.POST.get('Comments', '')
    
      LoadEDBGFoodObj = EBDGFOOD(EDBGDonorCompanyName=EDBGDonorCompanyName,DonorType=DonorType, 
                            FoodType=FoodType,Comments=Comments,ServingsperGallon=ServingsperGallon,
                         TotalValue =TotalValue ,  AverageCostperServing=AverageCostperServing,
                          ReceivedDate=ReceivedDate )
      LoadEDBGFoodObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/EDBG_Food_Donations.html',{})

def add_EmptyBowlFood(request):
    template_name = 'ics_tool/EB_Food.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EmptyBowlFoodDonationsform(request.POST)
    if form.is_valid():
    EBDonorCompanyName          = request.POST.get('EBDonorCompanyName', '')
    ContactPerson               = request.POST.get('ContactPerson ', '')
    FoodType                    = request.POST.get('FoodType', '')
    NumGallons                  = request.POST.get('NumGallons', '')
    TotalServing                = request.POST.get('TotalServing', '')
    ServingsperGallon           = request.POST.get('ServingsperGallon', '')
    AverageCost                 = request.POST.get('AverageCost', '')
    TotalValue                  = request.POST.get('TotalValue ', '')
    Comments                    = request.POST.get('Comments', '')
    
      LoadEBFoodObj = EMPTYBOWLFOOD(EBDonorCompanyName=EBDonorCompanyName, ContactPerson=ContactPerson, NumGallons=NumGallons , TotalServing=TotalServing,
                            FoodType=FoodType,Comments=Comments,ServingsperGallon=ServingsperGallon,
                         TotalValue =TotalValue ,  AverageCost=AverageCost,
                          ReceivedDate=ReceivedDate )
      LoadEBFoodObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/EB_Food.html',{})

def add_EmptyBowlRaffle(request):
    template_name = 'ics_tool/EB_Auction.html'

    if request.method == "GET":
        return render(request, template_name)

    form = EmptyBowlDonationsform(request.POST)
    if form.is_valid():
       DonorCompanyName             = request.POST.get('DonorCompanyName', '')
       Title                        = request.POST.get('Title ', '')
       ContactPerson                = request.POST.get('ContactPerson ', '')
       StreetAddress                = request.POST.get('StreetAddress', '')
       City                         = request.POST.get('City', '')
       State                        = request.POST.get('State', '')
       Zip                          = request.POST.get('Zip', '')
       PhoneNumber                  = request.POST.get('PhoneNumber', '')
       Email                        = request.POST.get('Email', '')
       DoantionDescription          = request.POST.get('DoantionDescription', '')
    EstimateValue                   = request.POST.get('EstimateValue', '')
    CommitteeContactPerson          = request.POST.get('CommitteeContactPerson', '')
    Salutation                      = request.POST.get('Salutation', '')
    Status                          = request.POST.get('Status', '')
    ReceivedDate                    = request.POST.get('ReceivedDate ', '')
    DonationFormReceived            = request.POST.get(' DonationFormReceived ', '')
      Comments                      = request.POST.get('Comments', '')
    
      LoadEBRaffObj = EMPTYBOWLRAFFLEAUCTION(DonorCompanyName=DonorCompanyName,Title=Title, ContactPerson= ContactPerson,
                            Email=Email,PhoneNumber=PhoneNumber,Comments=Comments,StreetAddress=StreetAddress,City=City,State=State,Zip=Zip,
                         DoantionDescription=DoantionDescription,  EstimateValue=EstimateValue ,CommitteeContactPerson=CommitteeContactPerson,
                          ReceivedDate=ReceivedDate,  Status=Status, Salutation=Salutation, DonationFormReceived=DonationFormReceived)
      LoadEBRaffObj.save()

      return render(request,'ics_tool/donor_success.html',{})

    print(form.errors)

    return render(request,'ics_tool/EB_Auction.html',{})







