from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    
    
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('add_event/', views.add_event, name='add_event'),
    path('view_events/', views.view_events, name='view_events'),
    path("edit-event/", views.edit_event, name="edit_event"),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
      
    
    path('add_vendor/', views.add_vendor, name='add_vendor'),
    path('view_vendors/', views.view_vendors, name='view_vendors'),
    path("get-vendors/<int:event_id>/", views.get_vendors, name="get_vendors"),
    path('edit_vendor/<int:vendor_id>/', views.edit_vendor, name='edit_vendor'),
    
    
    
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('view_tickets/', views.view_tickets, name='view_tickets'),
    path('get-tickets/<int:event_id>/', views.get_tickets, name='get_tickets'),
    path('update-ticket/', views.update_ticket, name='update_ticket'),
    path('delete-ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),

    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('view_schedules/', views.view_schedules, name='view_schedules'),
    path('get-schedules/<int:event_id>/', views.get_schedules, name='get_schedules'),
    path('update-schedule/<int:id>/', views.update_schedule, name='update_schedule'),
    path('delete-schedule/<int:id>/', views.delete_schedule, name='delete_schedule'),


    path('add_sponsor/', views.add_sponsor, name='add_sponsor'),
    path('view_sponsors/', views.view_sponsors, name='view_sponsors'),
    path('update-sponsor/<int:sponsor_id>/', views.edit_sponsor, name='edit_sponsor'),
    path('get-sponsors/<int:event_id>/', views.get_sponsors_for_event, name='get_sponsors_for_event'),
    path('delete-sponsor/<int:id>/', views.delete_sponsor, name='delete_sponsor'),

     path('add_attendee/', views.add_attendee, name='add_attendee'),
      path('get_ticket_types/', views.get_ticket_types, name='get_ticket_types'),
     path('view_attendees/', views.view_attendees, name='view_attendees'),
      path('get_attendees/<int:event_id>/', views.get_attendees, name='get_attendees'),
       path('update-attendee/<int:id>/', views.update_attendee, name='update_attendee'),
       path('get-tickets-for-event/<int:event_id>/', views.get_tickets_for_event, name='get_tickets_for_event'),
        path('delete-attendee/<int:attendee_id>/', views.delete_attendee, name='delete_attendee'),
    
    path('reports/', views.reports, name='reports'),
    
     path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),   
      

   
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
