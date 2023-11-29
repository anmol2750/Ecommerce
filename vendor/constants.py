class message:
    ADD_SUCCESS_MESSAGE = 'Vendor added Successfully.'
    UPDATE_SUCCESS_MESSAGE = 'Vendor Information Updated Successfully.'
    
class constants:
    ZERO = '0'
    ONE = '1'
    SEVEN = '7'


class vendorUrl:
    VENDOR_LIST_URL = 'vendor_list.html'
    ADD_VENDOR_URL = 'add_vendor.html'
    UPDATE_VENDOR_URL = 'update_vendor.html'
    VENDOR_DETAILS_URL = 'vendor_details.html'
    
    
class Form:
    ADD_FORM_FIELDS = ['logo', 'username', 'first_name', 'last_name', 'email']
    UPDATE_FORM_FIELDS = ['username', 'first_name', 'last_name']
    REQUIRED_ADDRESS_MESSAGE = 'Required. Enter your full address.'
    REQUIRED_COUNTRY_MESSAGE = 'Required. Select your Country.'
    REQUIRED_STATE_MESSAGE = 'Required. Select your State.'
    REQUIRED_CITY_MESSAGE = 'Required. Select your City.'
    REQUIRED_PINCODE_MESSAGE = 'Required. Enter your Pincode.'
    REQUIRED_EMAIL_MESSAGE = 'Required. Enter an email address.'
    REQUIRED_FIRST_NAME_MESSAGE = 'Required. Enter your First Name.'
    REQUIRED_USERNAME_MESSAGE = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
    REQUIRED_ADDRESS_TYPE_MESSAGE = 'Required. Select type of Address'
    EMAIL_ALREADY_EXISTS_ERROR = 'This email already exists. Please choose a different one.'
    USERNAME_ALREADY_EXISTS_ERROR = 'This username already exists. Please choose a different one.'
    COUNTRY_EMPTY_LABEL = "Select Country"
    STATE_EMPTY_LABEL = "State"
    CITY_EMPTY_LABEL = "City"

    