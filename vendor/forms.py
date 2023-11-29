from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from . import constants
from .models import Address, Country, State, City
from django.utils.translation import gettext_lazy as _
from django.db import connection

# Form for Adding a Vendor :
class AddVendorForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = constants.Form.ADD_FORM_FIELDS
        
    # Additional fields for the vendor logo. 
    logo =  forms.ImageField(help_text = 'Upload your Company logo')
    
    # Additional fields for the Address model. 
    address_line_1 = forms.CharField(max_length = 100, 
                                        required = True, 
                                        help_text = _(constants.Form.REQUIRED_ADDRESS_MESSAGE))
    
    address_line_2 = forms.CharField(max_length = 100, 
                                        required = False)
    
    country = forms.ModelChoiceField(required = True, 
                                        help_text = _(constants.Form.REQUIRED_COUNTRY_MESSAGE),
                                        queryset = Country.objects.all(),
                                        empty_label = _(constants.Form.COUNTRY_EMPTY_LABEL),
                                        widget = forms.Select(attrs = {'class' : 'form-control', 'id' : 'country'}))
    
    state = forms.IntegerField(required = True,
                                help_text = _(constants.Form.REQUIRED_STATE_MESSAGE),
                                label = _(constants.Form.STATE_EMPTY_LABEL),
                                widget = forms.Select(attrs = {'class' : 'form-control', 'id' : 'state'}))
    
    city = forms.IntegerField(required = True,
                                help_text = _(constants.Form.REQUIRED_CITY_MESSAGE),
                                label = _(constants.Form.CITY_EMPTY_LABEL),
                                widget = forms.Select(attrs = {'class' : 'form-control', 'id' : 'city'}))
    
    pincode = forms.CharField(max_length = 10, 
                                    required = True, 
                                    help_text = _(constants.Form.REQUIRED_PINCODE_MESSAGE))
    
    ADDRESS_TYPE_CHOICE = (('','Select type of Address'),('Work','Work'),('Home','Home')) 
    address_type = forms.ChoiceField(choices = ADDRESS_TYPE_CHOICE)
    
    username = forms.CharField(required = True,
                                label = _('Username'), 
                                help_text = _(constants.Form.REQUIRED_USERNAME_MESSAGE),
                                widget = forms.TextInput(attrs = {'class' : 'form-control', 'id' : 'username'}))
    
    email = forms.EmailField(required = True,
                                label = _('Email'), 
                                help_text = _(constants.Form.REQUIRED_EMAIL_MESSAGE),
                                widget = forms.TextInput(attrs = {'class' : 'form-control', 'id' : 'email'}))
    
    first_name = forms.CharField(required = True, 
                                    label = _('First name'), 
                                    help_text = _(constants.Form.REQUIRED_FIRST_NAME_MESSAGE),)

    
    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email__iexact = email).exists()
        if user:
            raise ValidationError(_(constants.Form.EMAIL_ALREADY_EXISTS_ERROR))
        return email
    
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact = username).exists():
            raise ValidationError(_(constants.Form.USERNAME_ALREADY_EXISTS_ERROR))
        return username
        
    
      
    
    