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
    
    
    path('add_ticket/', views.add_ticket, name='add_ticket'),
    path('view_tickets/', views.view_tickets, name='view_tickets'),

    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('view_schedules/', views.view_schedules, name='view_schedules'),

    path('add_sponsor/', views.add_sponsor, name='add_sponsor'),
    path('view_sponsors/', views.view_sponsors, name='view_sponsors'),

     path('add_attendee/', views.add_attendee, name='add_attendee'),
      path('get_ticket_types/', views.get_ticket_types, name='get_ticket_types'),
     path('view_attendees/', views.view_attendees, name='view_attendees'),
    
    path('reports/', views.reports, name='reports'),
    
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('logout/', views.logout_view, name='logout'),   
      

   
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
