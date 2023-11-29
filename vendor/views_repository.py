from django.contrib.auth.models import User
from django.conf import settings
from .models import Logo, Country, State, City, Address
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from . import constants
from .model_repository import LogoRepository, AddressRepository, UserRepository

class VendorRepository:
    
    def __init__(self):
        pass
    
    def filter_vendors(self, start_date, end_date):
        query = Q(is_superuser = constants.constants.ZERO)

        if start_date and end_date:
            query &= Q(date_joined__range = (start_date, end_date))

        return User.objects.filter(query).order_by("date_joined")

    def get_vendor_count(self):
        vendors = User.objects.filter(is_superuser = constants.constants.ZERO)
        return vendors.count()

    def get_active_vendor_count(self):
        vendor_active = User.objects.filter(is_superuser = constants.constants.ZERO, is_active = constants.constants.ONE)
        vendor_active_count = vendor_active.count()
        return vendor_active_count

    def get_inactive_vendor_count(self):
        vendor_inactive = User.objects.filter(is_superuser = constants.constants.ZERO, is_active = constants.constants.ZERO)
        vendor_inactive_count = vendor_inactive.count() 
        return vendor_inactive_count

    def get_paginator(self, request, vendors):
        paginator = Paginator(vendors, constants.constants.SEVEN)
        page = request.GET.get('page')
        vendor = paginator.get_page(page)
        return vendor
    
    def create_vendor(self, form):
        # Create a new user
        user_repository = UserRepository()
        user = user_repository.create_user(form)
        # Save logo in the Logo table.
        logo_repository = LogoRepository()
        logo_repository.save_logo(user, form.cleaned_data['logo'])
        # Save address information in the Vendor Address table.
        address_repository = AddressRepository()
        address_repository.save_address(user, form.cleaned_data)
        return user

    def update_vendor(self, user, address, logo, request):
        # Update user information in the auth_user table
        user_repository = UserRepository()
        user_repository.update_user(user, request)
        # Update address information in the address table
        address_repository = AddressRepository()
        address_repository.update_address(address, request)
        # Update logo information in the logo table.
        logo_repository = LogoRepository()
        logo_repository.update_logo(logo, request)

    def get_vendor_details(self, id):
        address_repository = AddressRepository()
        address = address_repository.get_address_by_user(id)
        logo_repository = LogoRepository()
        logo = logo_repository.get_logo_by_user(id)
        return address, logo

    def delete_vendor():
        pass