from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length = 100)
    code = models.CharField(max_length = 20, default = None)
    phonecode = models.CharField(max_length = 15, default = None)

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
        
    def __str__(self):
        return self.name
    
    
class State(models.Model):
    name = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, default = None, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'state'
        verbose_name_plural = 'states'
    
    def __str__(self):
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length = 100)
    state = models.ForeignKey(State, default = None, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'
    
    def __str__(self):
        return self.name
    
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    address_line_1 = models.CharField(max_length = 100)
    address_line_2 = models.CharField(max_length = 100)
    country = models.ForeignKey(Country, on_delete = models.CASCADE)
    state = models.ForeignKey(State, on_delete = models.CASCADE)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    pincode = models.CharField(max_length = 10)
    address_type = models.CharField(max_length = 25, default = None)
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
    
    def __str__(self):
        return f"{self.address_line_1}, {self.country}, {self.state}, {self.city}, {self.pincode}"


class Logo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    logo = models.ImageField(upload_to = "images/vendor_logo", null = True, blank = True)
    is_deleted = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = 'logo'
        verbose_name_plural = 'logos'
        
    def __str__(self):
        return self.user.username
    
    
    
