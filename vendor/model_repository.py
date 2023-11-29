from .models import Country, State, City, Address, Logo
from django.contrib.auth.models import User
from django.conf import settings


class UserRepository:
    
    def get_all_users():
        return User.objects.all()

    def get_user_by_id(user_id):
        return User.objects.get(pk = user_id)
        
    def create_user(self, form):    
        user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
            )
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        if settings.ENABLE_USER_ACTIVATION:
            user.is_active = False
        user.save()
        return user
    
    def update_user(self, user, request):
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.save()
            

class AddressRepository:
    
    def get_all_addresses():
        return Address.objects.all()
    
    def get_address_by_id(address_id):
        return Address.objects.get(pk = address_id)
    
    def get_address_by_user(self, user_id):
        return Address.objects.get(user_id = user_id)
    
    def save_address(self, user, cleaned_data):
        address = Address(
            user = user,
            address_line_1 = cleaned_data['address_line_1'],
            address_line_2 = cleaned_data['address_line_2'],
            country = cleaned_data['country'],
            state = State.objects.get(id = cleaned_data['state']),
            city = City.objects.get(id = cleaned_data['city']),
            pincode = cleaned_data['pincode'],
            address_type = cleaned_data['address_type']
        )
        address.save()
        
    def update_address(self, address, request):
        address.address_line_1 = request.POST['addressline1']
        address.address_line_2 = request.POST['addressline2']
        address.country = Country.objects.get(id=request.POST['country'])
        address.state = State.objects.get(id=request.POST['state'])
        address.city = City.objects.get(id=request.POST['city'])
        address.pincode = request.POST['pincode']
        address.save()
    
    def delete_address(address_id):
        address = Address.objects.get(pk = address_id)
        address.delete()
        
    
class LogoRepository:
        
    def get_logo_by_user(self, user_id):
        return Logo.objects.get(user_id = user_id)
    
    def save_logo(self, user, logo):
        logo = Logo(user = user, logo = logo)
        logo.save()

    def update_logo(self, logo, request):
        if 'logo' in request.FILES:
            logo.logo = request.FILES.get('logo')
            logo.save()
    
    def delete_logo(user):
        logo_instance = Logo.objects.filter(user = user).first()
        if logo_instance:
            logo_instance.delete()
            

class CountryRepository:
    
    def get_all_countries():
        return Country.objects.all()
    
    def get_country_by_id(country_id):
        return Country.objects.get(pk = country_id)
    
    def create_country(name, code = None, phonecode = None):
        return Country.objects.create(name = name, code = code, phonecode = phonecode)
    
    def update_country(country_id, name, code = None, phonecode = None):
        country = Country.objects.get(pk = country_id)
        country.name = name
        country.code = code
        country.phonecode = phonecode
        country.save()
        return country
    
    def delete_country(country_id):
        country = Country.objects.get(pk = country_id)
        country.delete()
        
        
class StateRepository:
    
    def get_all_states():
        return State.objects.all()
    
    def get_state_by_id(state_id):
        return State.objects.get(pk = state_id)
    
    def create_state(name, country):
        return State.objects.create(name = name, country = country)
    
    def update_state(state_id, name, country):
        state = State.objects.get(pk = state_id)
        state.name = name
        state.country = country
        state.save()
        return state
    
    def delete_state(state_id):
        state = State.objects.get(pk = state_id)
        state.delete()
        
        
class CityRepository:
    
    def get_all_cities():
        return City.objects.all()
    
    def get_city_by_id(city_id):
        return City.objects.get(pk = city_id)
    
    def create_city(name, state):
        return City.objects.create(name = name, state = state)
    
    def update_city(city_id, name, state):
        city = City.objects.get(pk = city_id)
        city.name = name
        city.state = state
        city.save()
        return city
    
    def delete_city(city_id):
        city = City.objects.get(pk = city_id)
        city.delete()