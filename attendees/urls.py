from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('attendee_home/', views.attendee_home, name='attendee_home'),

     path('event/<int:event_id>/buy-tickets/', views.ticket_buying_page, name='ticket_buying_page'),
     path('submit_ticket_details/', views.submit_ticket_details, name='submit_ticket_details'),
     path('contact_page/', views.contact_page, name='contact_page'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    
   
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
