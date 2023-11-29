from django.urls import path
from . import views

# Application Name.
app_name = 'vendor'


urlpatterns = [
    # Vendor List URL :
    path('', views.vendorListView.as_view(), name = 'vendor_list'),
    
    # Add Vendor URL :
    path('addvendor/', views.vendorAddView.as_view(), name = 'add_vendor'),
    
    # Update Vendor URL :
    path('updatevendor/<int:id>', views.vendorUpdateView.as_view(), name = 'update_vendor'),
    
    # Vendor Details URL :
    path('vendordetails/<int:id>', views.vendorDetailsView.as_view(), name = 'vendor_details'),
    
    # Accept and Reject Vendor URL : 
    path('action/', views.actionVendorView.as_view(), name = 'action_vendor'),
    
    # URL for fetching state :
    path('get_state/', views.get_state.as_view(), name = 'get_state'),
    
    # URL for fetching city :
    path('get_city/', views.get_city.as_view(), name = 'get_city'),
    
    # Username Exist URL :
    path('username_exists/', views.username_exists.as_view(), name = 'username_exists'),
    
    # Email Exist URL :
    path('email_exists/', views.email_exists.as_view(), name = 'email_exists'),
    
    # Live search URL :
    path('search/', views.search.as_view(), name = 'search'),

#     Delete Vendor URL :
#     path('deletevendor/<int:id>', views.deleteVendorView, name = 'delete_vendor'),
]