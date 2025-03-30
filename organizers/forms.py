
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User  # Use the default User model
        fields = ['username', 'email', 'password']  # Fields for user Signup

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            EmailValidator()(email)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 or not any(char.isdigit() for char in password) \
                or not any(char.isupper() for char in password) or not any(char in '!@#$%^&*()' for char in password):
            raise ValidationError("Password must be at least 8 characters long, contain an uppercase letter, a number, and a symbol.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match.")




class SigninForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
# forms.py
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_type', 'event_description', 'event_theme', 'event_date', 'venue', 'setup_time', 'breakdown_time']


from django import forms
from .models import Vendor, Venue, Catering, AV, Decor, Entertainment, Security, Printing, Transportation, WasteManagement

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'vendor_type', 'description']

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['venue_address', 'venue_capacity', 'venue_booking_time', 'venue_rental_cost', 'venue_requirements']

class CateringForm(forms.ModelForm):
    class Meta:
        model = Catering
        fields = ['catering_type', 'menu_options', 'dietary_preferences', 'catering_cost', 'service_requirements']

class AVForm(forms.ModelForm):
    class Meta:
        model = AV
        fields = ['equipment_provided', 'av_cost', 'technical_support', 'setup_time', 'contact_emergency']

class DecorForm(forms.ModelForm):
    class Meta:
        model = Decor
        fields = ['design_theme', 'items_supplied', 'decor_cost', 'setup_time', 'return_tear_down_time']

class EntertainmentForm(forms.ModelForm):
    class Meta:
        model = Entertainment
        fields = ['type_of_entertainment', 'entertainment_cost', 'performance_duration', 'special_requirements']

class SecurityForm(forms.ModelForm):
    class Meta:
        model = Security
        fields = ['security_personnel_count', 'security_duties', 'security_cost', 'setup_requirements']

class PrintingForm(forms.ModelForm):
    class Meta:
        model = Printing
        fields = ['printed_materials', 'printing_cost', 'design_requirements', 'delivery_timeframe']

class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ['transport_type', 'transportation_cost', 'transport_schedule', 'passenger_capacity', 'special_requests']

class WasteManagementForm(forms.ModelForm):
    class Meta:
        model = WasteManagement
        fields = ['waste_types_collected', 'waste_management_cost', 'service_details', 'restroom_facilities']
