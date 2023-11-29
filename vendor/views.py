from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from . import constants
from .forms import AddVendorForm
from django.utils.crypto import get_random_string
from django.conf import settings
from .models import Address, Country, State, City, Logo
from django.http import JsonResponse
from django.contrib import messages 
from .views_repository import VendorRepository
from django.views import View


#  Vendor List View :
class vendorListView(View):
    template_name = constants.vendorUrl.VENDOR_LIST_URL
    
    def get(self, request):
        start_date = request.GET.get('startdate', '')
        end_date = request.GET.get('enddate', '')
        
        vendor_list_repository = VendorRepository()
        vendors = vendor_list_repository.filter_vendors(start_date, end_date)
        vendor_count = vendor_list_repository.get_vendor_count()
        vendor_active_count = vendor_list_repository.get_active_vendor_count()
        vendor_inactive_count = vendor_list_repository.get_inactive_vendor_count()
        vendor = vendor_list_repository.get_paginator(request, vendors)
        context = {
            'object'               : vendor,
            'vendor_count'         : vendor_count,
            'vendor_active_count'  : vendor_active_count,
            'vendor_inactive_count': vendor_inactive_count,
        }
        return render(request, self.template_name, context)
    

# Add Vendor View : 
class vendorAddView(View):
    template_name = constants.vendorUrl.ADD_VENDOR_URL 
    
    def get(self, request):
        form = AddVendorForm()
        context = {   
            'form' : form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AddVendorForm(request.POST, request.FILES)
        if form.is_valid():
            create_vendor_repository = VendorRepository()             # Import and instantiate VendorRepository
            user = create_vendor_repository.create_vendor(form)
            messages.success(request, constants.message.ADD_SUCCESS_MESSAGE)
            return redirect('vendor:vendor_list')                     # Redirect to the vendor list page
        else:
            context = {
                'form' : form,
            }
            return render(request, self.template_name, context)


# Update Vendor View :
class vendorUpdateView(View):
    template_name = constants.vendorUrl.UPDATE_VENDOR_URL
    
    def get(self, request, id):
        user = get_object_or_404(User, pk = id)
        address = Address.objects.get(user = user)
        logo = Logo.objects.get(user = user)
        countries = Country.objects.all()
        states = State.objects.filter(country = address.country)
        cities = City.objects.filter(state = address.state)
        context = {
            'user'      : user,
            'address'   : address,
            'logo'      : logo,
            'countries' : countries,
            'states'    : states,
            'cities'    : cities,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, id):
        user = get_object_or_404(User, pk = id)
        address = Address.objects.get(user = user)
        logo = Logo.objects.get(user = user)
        countries = Country.objects.all()
        states = State.objects.filter(country = address.country)
        cities = City.objects.filter(state = address.state)
        
        if request.method == 'POST':
            update_vendor_repository = VendorRepository()           # Import and instantiate VendorRepository
            update_vendor_repository.update_vendor(user, address, logo, request)
            messages.success(request, constants.message.UPDATE_SUCCESS_MESSAGE)
            return redirect('vendor:vendor_list')                   # Redirect to Vendor List Page. 
        context = {
            'user'      : user,
            'address'   : address,
            'logo'      : logo,
            'countries' : countries,
            'states'    : states,
            'cities'    : cities,
        }
        return render(request, self.template_name, context)


# To show vendor Data. 
class vendorDetailsView(View):
    template_name = constants.vendorUrl.VENDOR_DETAILS_URL
    
    def get(self, request, id):
        vendor_details_repository = VendorRepository()               # Import and instantiate VendorRepository
        address, logo = vendor_details_repository.get_vendor_details(id)
        context = {
            'address'             : address,
            'logo'                : logo,
        }
        return render(request, self.template_name, context)
    

# Action(accept and Reject) Vendor View.
class actionVendorView(View):
    
    def post(self, request):
        if request.method == 'POST':
            id_ = request.POST['id_']
            action = request.POST['action']
            vendor = User.objects.get(pk = id_)
            
            if action == 'accept':
                vendor.is_active = True
            elif action == 'reject':
                vendor.is_active = False
            vendor.save()  
        return redirect("vendor:vendor_list")


# For Fetching states related to Country :
class get_state(View):
    
    def get(self, request):
        country_id = request.GET.get('country_id')
        if country_id:
            states = State.objects.filter(country_id = country_id)
            state = [{'id' : state.id, 'name' : state.name} for state in states]
        else:
            state = []
        return JsonResponse({'states': state})   


# For Fetching cities related to States :
class get_city(View):
    
    def get(self, request):
        state_id = request.GET.get('state_id')
        if state_id:
            cities = City.objects.filter(state_id = state_id)
            city = [{'id' : city.id, 'name' : city.name} for city in cities]
        else:
            city = [] 
        return JsonResponse({'city' : city})      


# Validation : Username already exists.
class username_exists(View):
    
    def get(self, request):
        username = request.GET.get('username', None)
        data = {
            'exists' : User.objects.filter(username__iexact = username).exists(),
        }
        return JsonResponse(data)


# Validation : Email already exists.
class email_exists(View):
    
    def get(self, request):
        email = request.GET.get('email', None)
        data = {
            'exists' : User.objects.filter(email__iexact = email).exists(),
        }
        return JsonResponse(data)


# Live Searching. 
class search(View):
    
    def get(self, request):
        query = request.GET.get('query', '')
        results = Logo.objects.filter(user__username__icontains = query, user__is_superuser = constants.zero)
        data = [
            {
                'id'         : result.user.id,
                'date_joined': result.user.date_joined.strftime('%Y-%m-%d'),
                'logo'       : result.logo.url if result.logo else '',
                'username'   : result.user.username,
                'email'      : result.user.email,
                'first_name' : result.user.first_name,
                'last_name'  : result.user.last_name,
                'is_active'  : result.user.is_active,
            } for result in results
        ]
        return JsonResponse(data, safe = False)














