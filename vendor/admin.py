from django.contrib import admin
from .models import Address, Country, State, City, Logo

admin.site.register(Address)

admin.site.register(Country)

admin.site.register(State)

admin.site.register(City)

admin.site.register(Logo)