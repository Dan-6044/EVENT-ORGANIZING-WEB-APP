# models.py
from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    EVENT_TYPES = [
         ('Theater', 'Theater'),
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('concert', 'Concert'),
        ('wedding', 'Wedding'),
        ('corporate', 'Corporate Event'),
    ]

    event_name = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    event_description = models.TextField()
    event_theme = models.CharField(max_length=255, blank=True, null=True)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    setup_time = models.DateTimeField()
    breakdown_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link event to user
    poster = models.ImageField(upload_to='event_posters/', null=True, blank=True)

    def __str__(self):
        return self.event_name


from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    VENDOR_TYPES = (
        ('venue', 'Venue'),
        ('catering', 'Catering'),
        ('av', 'AV Equipment'),
        ('decor', 'Decor'),
        ('entertainment', 'Entertainment'),
        ('security', 'Security'),
        ('printing', 'Printing'),
        ('transportation', 'Transportation'),
        ('waste_management', 'Waste Management'),
    )

    name = models.CharField(max_length=255)
    vendor_type = models.CharField(max_length=20, choices=VENDOR_TYPES)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate vendor with user

    def __str__(self):
        return self.name


class Venue(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    venue_address = models.CharField(max_length=255)
    venue_capacity = models.IntegerField()
    venue_booking_time = models.DateTimeField()
    venue_rental_cost = models.DecimalField(max_digits=10, decimal_places=2)
    venue_requirements = models.TextField(blank=True)

    def __str__(self):
        return f"Venue - {self.vendor.name}"


class Catering(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    catering_type = models.CharField(max_length=100)
    menu_options = models.TextField()
    dietary_preferences = models.CharField(max_length=255, blank=True)
    catering_cost = models.DecimalField(max_digits=10, decimal_places=2)
    service_requirements = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Catering - {self.vendor.name}"


class AV(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    equipment_provided = models.CharField(max_length=255)
    av_cost = models.DecimalField(max_digits=10, decimal_places=2)
    technical_support = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')])
    setup_time = models.TimeField()
    contact_emergency = models.CharField(max_length=15)

    def __str__(self):
        return f"AV Equipment - {self.vendor.name}"


class Decor(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    design_theme = models.CharField(max_length=255)
    items_supplied = models.TextField()
    decor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    setup_time = models.TimeField()
    return_tear_down_time = models.TimeField()

    def __str__(self):
        return f"Decor - {self.vendor.name}"


class Entertainment(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    type_of_entertainment = models.CharField(max_length=255)
    entertainment_cost = models.DecimalField(max_digits=10, decimal_places=2)
    performance_duration = models.DurationField()
    special_requirements = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Entertainment - {self.vendor.name}"


class Security(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    security_personnel_count = models.IntegerField()
    security_duties = models.TextField()
    security_cost = models.DecimalField(max_digits=10, decimal_places=2)
    setup_requirements = models.TextField()

    def __str__(self):
        return f"Security - {self.vendor.name}"


class Printing(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    printed_materials = models.TextField()
    printing_cost = models.DecimalField(max_digits=10, decimal_places=2)
    design_requirements = models.TextField()
    delivery_timeframe = models.DateTimeField()

    def __str__(self):
        return f"Printing - {self.vendor.name}"


class Transportation(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    transport_type = models.CharField(max_length=255)
    transportation_cost = models.DecimalField(max_digits=10, decimal_places=2)
    transport_schedule = models.TextField()
    passenger_capacity = models.IntegerField()
    special_requests = models.TextField()

    def __str__(self):
        return f"Transportation - {self.vendor.name}"


class WasteManagement(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    waste_types_collected = models.TextField()
    waste_management_cost = models.DecimalField(max_digits=10, decimal_places=2)
    service_details = models.TextField()
    restroom_facilities = models.TextField()

    def __str__(self):
        return f"Waste Management - {self.vendor.name}"


from django.db import models

class Ticket(models.Model):
    TICKET_TYPES = [
        ('regular', 'Regular'),
        ('early_bird', 'Early Bird'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP'),
    ]
    
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='tickets')    
    ticket_type = models.CharField(max_length=20, choices=TICKET_TYPES, default='regular')
    ticket_description = models.TextField()    
    early_bird_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vip_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vvip_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_quantity = models.PositiveIntegerField()
    available_quantity = models.PositiveIntegerField()
    min_quantity = models.PositiveIntegerField()
    max_quantity = models.PositiveIntegerField()
    early_bird_expiry_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.ticket_type


from django.db import models
from django.contrib.auth.models import User
from .models import Event

class EventSchedule(models.Model):
    event = models.ForeignKey(Event, related_name='schedules', on_delete=models.CASCADE)
    session_type = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.event.event_name} - {self.session_type} ({self.start_time} - {self.end_time})"


class Sponsor(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="sponsors")
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sponsor_logos/')
    description = models.TextField()
    website_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    description = models.TextField(null=True, blank=True)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
