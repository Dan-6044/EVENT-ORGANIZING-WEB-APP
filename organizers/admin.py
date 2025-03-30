# admin.py
from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_type', 'event_date', 'venue')
    search_fields = ('event_name', 'venue')
    list_filter = ('event_type', 'event_date')

admin.site.register(Event, EventAdmin)



from django.contrib import admin
from .models import Vendor, Venue, Catering, AV, Decor, Entertainment, Security, Printing, Transportation, WasteManagement

class VenueAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'venue_address', 'venue_capacity', 'venue_booking_time', 'venue_rental_cost')
    search_fields = ('vendor__name', 'venue_address')

class CateringAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'catering_type', 'catering_cost')
    search_fields = ('vendor__name', 'catering_type')

class AVAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'equipment_provided', 'av_cost', 'technical_support', 'setup_time')
    search_fields = ('vendor__name', 'equipment_provided')

class DecorAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'design_theme', 'decor_cost', 'setup_time')
    search_fields = ('vendor__name', 'design_theme')

class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'type_of_entertainment', 'entertainment_cost', 'performance_duration')
    search_fields = ('vendor__name', 'type_of_entertainment')

class SecurityAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'security_personnel_count', 'security_cost')
    search_fields = ('vendor__name', 'security_personnel_count')

class PrintingAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'printed_materials', 'printing_cost', 'delivery_timeframe')
    search_fields = ('vendor__name', 'printed_materials')

class TransportationAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'transport_type', 'transportation_cost', 'passenger_capacity')
    search_fields = ('vendor__name', 'transport_type')

class WasteManagementAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'waste_types_collected', 'waste_management_cost')
    search_fields = ('vendor__name', 'waste_types_collected')

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor_type', 'description')
    search_fields = ('name',)
    list_filter = ('vendor_type',)

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Catering, CateringAdmin)
admin.site.register(AV, AVAdmin)
admin.site.register(Decor, DecorAdmin)
admin.site.register(Entertainment, EntertainmentAdmin)
admin.site.register(Security, SecurityAdmin)
admin.site.register(Printing, PrintingAdmin)
admin.site.register(Transportation, TransportationAdmin)
admin.site.register(WasteManagement, WasteManagementAdmin)


from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = [ 'ticket_type',  'total_quantity', 'available_quantity', 'event']
    list_filter = ['ticket_type', 'event']
    search_fields = ['ticket_name', 'ticket_type', 'ticket_description']
    list_editable = [ 'total_quantity', 'available_quantity']
    
    # Display the fields in the detail view
    fieldsets = (
        (None, {
            'fields': ( 'ticket_type', 'ticket_description', 'event')
        }),
        ('Pricing Information', {
            'fields': ( 'early_bird_price', 'vip_price', 'vvip_price'),
        }),
        ('Availability', {
            'fields': ('total_quantity', 'available_quantity', 'min_quantity', 'max_quantity'),
        }),
        ('Early Bird Information', {
            'fields': ('early_bird_expiry_date',),
        }),
    )

admin.site.register(Ticket, TicketAdmin)

from .models import EventSchedule

# EventSchedule admin
class EventScheduleAdmin(admin.ModelAdmin):
    list_display = ('event', 'session_type', 'start_time', 'end_time', 'description')
    search_fields = ('event__name', 'session_type')
    list_filter = ('event', 'session_type')

admin.site.register(EventSchedule, EventScheduleAdmin)

# admin.py
from django.contrib import admin
from .models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    # Displaying fields in the admin interface
    list_display = ('name', 'event', 'description', 'website_url', 'logo_thumbnail')
    search_fields = ('name', 'event__event_name')  # Allow search by event name and sponsor name
    list_filter = ('event',)  # Filter by event
    list_per_page = 20  # Number of sponsors per page in the admin interface
    
    # Method to display the logo image in the admin list view
    def logo_thumbnail(self, obj):
        return f'<img src="{obj.logo.url}" width="50" height="50" />'
    logo_thumbnail.allow_tags = True
    logo_thumbnail.short_description = 'Logo'

admin.site.register(Sponsor, SponsorAdmin)

# admin.py

from django.contrib import admin
from .models import Attendee

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('event', 'ticket', 'name', 'email', 'phone_number', 'ticket_price', 'discount_percentage', 'description')
    search_fields = ('name', 'email', 'phone_number', 'event__event_name', 'ticket__ticket_type')
    list_filter = ('event', 'ticket', 'ticket__ticket_type')
    ordering = ('-event',)

admin.site.register(Attendee, AttendeeAdmin)


