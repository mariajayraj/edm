from django import forms
from django.conf import settings
from .models import *

class CustomerForm(forms.ModelForm):
    CustomerId    = forms.IntegerField()
    CustomerName  = forms.CharField(max_length=10)

    class Meta:
        model = Customer
        fields = '__all__'

class AddDonorForm(forms.ModelForm):
    OrganizationName    = forms.CharField(max_length=100)
    Salutation          = forms.CharField(max_length=100)
    FirstName           = forms.CharField(max_length=100)
    LastName            = forms.CharField(max_length=100)
    Email               = forms.EmailField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    Comments            = forms.CharField(max_length=100,required=False)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    ICS                 = forms.CharField(max_length=2,required=False)

    class Meta:
        model = Donors
        fields = '__all__'

class SearchDonorForm(forms.ModelForm):
    SearchQuery = forms.CharField(max_length=255)

    class Meta:
        model = SearchDonor
        fields = '__all__'

class GolfAddDonationsform(forms.ModelForm):
    CompanyName         = forms.CharField(max_length=100)
    Title               = forms.CharField(max_length=100)
    DonorContactPerson  = forms.CharField(max_length=100)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    Email               = forms.EmailField(max_length=100)
    DoantionDescription = forms.CharField(max_length=100)
    EstimateValue       = forms.CharField(max_length=100)
    UserContactPerson   = forms.CharField(max_length=100)
    ReceivedDate        = forms.CharField(max_length=100)
    DonationType        = forms.CharField(max_length=100)
    Comments            = forms.CharField(max_length=100,required=False)
    
    class Meta:
        model = Golf
        fields = '__all__'
        
 class EDBGRaffleDonationsform(forms.ModelForm):
    DonorCompanyName         = forms.CharField(max_length=100)
    Title               = forms.CharField(max_length=100)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    Email               = forms.EmailField(max_length=100)
    DoantionDescription = forms.CharField(max_length=100)
    EstimateValue       = forms.CharField(max_length=100)
    ReceivedDate        = forms.CharField(max_length=100)
    Comments            = forms.CharField(max_length=100,required=False)
    
    class Meta:
        model = EBDGRAFFLE
        fields = '__all__'
        
    class EDBGFoodDonationsform(forms.ModelForm):
    EDBGDonorCompanyName    = forms.CharField(max_length=100)
    DonorType               = forms.CharField(max_length=100)
    FoodType                = forms.CharField(max_length=100)
    ServingsperGallon       = forms.CharField(max_length=100)
    AverageCostperServing   = forms.CharField(max_length=100)
    TotalValue              = forms.CharField(max_length=100)
    Comments                = forms.CharField(max_length=100,required=False)
    
    class Meta:
        model = EBDGFOOD
        fields = '__all__'
        
    class EmptyBowlFoodDonationsform(forms.ModelForm):
    EBDonorCompanyName      = forms.CharField(max_length=100)
    ContactPerson           = forms.CharField(max_length=100)
    FoodType                = forms.CharField(max_length=100)
    NumGallons              = forms.CharField(max_length=100)
    ServingsperGallon       = forms.CharField(max_length=100)
    TotalServing            = forms.CharField(max_length=100)
    AverageCost             = forms.CharField(max_length=100)
    TotalValue              = forms.CharField(max_length=100)
    Comments                = forms.CharField(max_length=100,required=False)
    
    class Meta:
        model = EMPTYBOWLFOOD
        fields = '__all__'
        
    class EmptyBowlDonationsform(forms.ModelForm):
    DonorCompanyName    = forms.CharField(max_length=100)
    ContactPerson           = forms.CharField(max_length=100)
    Title               = forms.CharField(max_length=100)
    StreetAddress       = forms.CharField(max_length=100)
    City                = forms.CharField(max_length=100)
    State               = forms.CharField(max_length=100)
    Zip                 = forms.CharField(max_length=100)
    PhoneNumber         = forms.CharField(max_length=15)
    Email               = forms.EmailField(max_length=100)
    DoantionDescription = forms.CharField(max_length=100)
    EstimateValue       = forms.CharField(max_length=100)
    CommitteeContactPerson  = forms.CharField(max_length=100)
    Salutation          = forms.CharField(max_length=100)
    Status              = forms.CharField(max_length=100)
    ReceivedDate        = forms.CharField(max_length=100)
    DonationFormReceived  = forms.CharField(max_length=100)
    Comments            = forms.CharField(max_length=100,required=False)
    
    class Meta:
        model = EMPTYBOWLRAFFLEAUCTION
        fields = '__all__'
        
    
        
    

    
    
