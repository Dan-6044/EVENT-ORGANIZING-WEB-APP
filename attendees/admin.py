# admin.py
from django.contrib import admin
from .models import ContactMessage

# Customize the admin interface for ContactMessage
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Display these fields in the list view
    search_fields = ('name', 'email', 'message')  # Add search functionality to these fields
    list_filter = ('email',)  # Filter options based on email (can be changed to other fields)
    ordering = ('-id',)  # Order the messages by ID in descending order (most recent first)

admin.site.register(ContactMessage, ContactMessageAdmin)
