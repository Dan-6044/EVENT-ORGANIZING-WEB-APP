 
from django.shortcuts import render, redirect
from django.contrib.auth import  authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm  # You can also create a ModelForm to simplify



def home(request):    
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create the new user
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user_id = user.id  # Get the user's ID

            # Log the user in automatically after registration
            login(request, user)
            return redirect('dashboard')  # Redirect to home after successful registration
        else:
            # Pass the form errors to the template
            return render(request, 'signing.html', {'form': form, 'signup_errors': form.errors})

    else:
        form = SignupForm()

    return render(request, 'signing.html', {'form': form})

def signin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Ensure email and password are provided
        if not email or not password:
            messages.error(request, "Both email and password are required.", extra_tags="login_error")
            return redirect('signin')

        # Get user by email
        user = User.objects.filter(email=email).first()

        if user:
            authenticated_user = authenticate(request, username=user.username, password=password)
            if authenticated_user:
                auth_login(request, authenticated_user)
                return redirect(reverse('dashboard'))  # Redirect to dashboard
            else:
                messages.error(request, "Invalid email or password.", extra_tags="login_error")
        else:
            messages.error(request, "Invalid email or password.", extra_tags="login_error")

    return render(request, 'signing.html')  # Ensure the correct template name



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Event

@login_required
def add_event(request):
    if request.method == 'POST':
        # Get form data from the request
        event_name = request.POST['event_name']
        event_type = request.POST['event_type']
        event_description = request.POST['event_description']
        event_theme = request.POST['event_theme']
        event_date = request.POST['event_date']
        venue = request.POST['venue']
        setup_time = request.POST['setup_time']
        breakdown_time = request.POST['breakdown_time']
        poster = request.FILES.get('poster')  # Get the uploaded poster

        # Check if an event with the same name, date, and venue already exists for the logged-in user
        if Event.objects.filter(
            event_name=event_name,
            event_date=event_date,
            venue=venue,
            user=request.user
        ).exists():
            # If event exists, display an error message
            messages.error(request, "An event with the same name, date, and venue already exists.")
            return redirect('add_event')  # Redirect back to the event creation page

        # Create a new Event instance and associate it with the logged-in user
        event = Event(
            event_name=event_name,
            event_type=event_type,
            event_description=event_description,
            event_theme=event_theme,
            event_date=event_date,
            venue=venue,
            setup_time=setup_time,
            breakdown_time=breakdown_time,
            user=request.user,
            poster=poster
        )

        # Save the event to the database
        event.save()

        # Redirect to a success page or event list after adding the event
        return redirect('view_events')  # Adjust this to your actual event list URL or a success page

    return render(request, 'create_event.html')  # Render the event creation form



@login_required
def view_events(request):
    # Filter events related to the logged-in user
    events = Event.objects.filter(user=request.user)  # Only get events where the user is the logged-in user
    return render(request, 'view_events.html', {'events': events})



from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Event

def edit_event(request):
    if request.method == "POST":
        event_id = request.POST.get("event_id")
        event = get_object_or_404(Event, id=event_id)

        # Update event details
        event.event_name = request.POST.get("event_name")
        event.event_type = request.POST.get("event_type")
        event.event_description = request.POST.get("event_description")
        event.event_theme = request.POST.get("event_theme")
        event.event_date = request.POST.get("event_date")
        event.venue = request.POST.get("venue")
        event.setup_time = request.POST.get("setup_time")
        event.breakdown_time = request.POST.get("breakdown_time")

        # Handle poster upload
        if "poster" in request.FILES:
            event.poster = request.FILES["poster"]

        event.save()
        messages.success(request, "Event updated successfully!")
        return redirect("view_events")  # Redirect to your events page

    messages.error(request, "Invalid request.")
    return redirect("events_page")



from django.shortcuts import render, get_object_or_404, redirect
from .models import Event

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('view_events')  # Redirect back to the events list after deletion





from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Vendor, Venue, Catering, AV, Decor, Entertainment, Security, Printing, Transportation, WasteManagement, Event

@login_required
def add_vendor(request):
    if request.method == 'POST':
        # Capture the vendor information from the form
        vendor_name = request.POST.get('name')
        vendor_type = request.POST.get('vendor_type')
        vendor_description = request.POST.get('event_description')
        payment_cost = request.POST.get('payment_cost')
        deposit = request.POST.get('deposit')
        credit_days = request.POST.get('credit_days')
        payment_status = request.POST.get('payment_status')
        event_id = request.POST.get('event_name')  # Event selected for this vendor
      

        # Ensure that all required fields are present
        if not vendor_name or not vendor_type or not vendor_description or not event_id:
            return render(request, 'add_vendor.html', {'error': 'All fields are required.'})
        
        event = get_object_or_404(Event, id=event_id)  # This ensures event_id exists

        # Save the vendor details in the Vendor table
        vendor = Vendor(
            name=vendor_name,
            vendor_type=vendor_type,
            description=vendor_description,
            payment_cost=payment_cost,
            deposit=deposit,
            credit_days=credit_days,
            payment_status=payment_status,
            user=request.user,  # Associate vendor with logged-in user
             event=event
        )
        vendor.save()

        # Handle vendor-specific details based on vendor type
        if vendor_type == 'venue':
            venue_address = request.POST.get('venue_address')
            venue_capacity = request.POST.get('venue_capacity')
            venue_booking_time = request.POST.get('venue_booking_time')
            venue_rental_cost = request.POST.get('venue_rental_cost')
            venue_requirements = request.POST.get('venue_requirements', '')

            venue = Venue(
                vendor=vendor,
                venue_address=venue_address,
                venue_capacity=venue_capacity,
                venue_booking_time=venue_booking_time,
                venue_rental_cost=venue_rental_cost,
                venue_requirements=venue_requirements
            )
            venue.save()

        elif vendor_type == 'catering':
            catering_type = request.POST.get('catering_type')
            menu_options = request.POST.get('menu_options')
            dietary_preferences = request.POST.get('dietary_preferences', '')
            catering_cost = request.POST.get('catering_cost')
            service_requirements = request.POST.get('service_requirements', '')

            catering = Catering(
                vendor=vendor,
                catering_type=catering_type,
                menu_options=menu_options,
                dietary_preferences=dietary_preferences,
                catering_cost=catering_cost,
                service_requirements=service_requirements
            )
            catering.save()

        elif vendor_type == 'av':
            equipment_provided = request.POST.get('equipment_provided')
            av_cost = request.POST.get('av_cost')
            technical_support = request.POST.get('technical_support')
            setup_time = request.POST.get('setup_time')
            contact_emergency = request.POST.get('contact_emergency')

            av = AV(
                vendor=vendor,
                equipment_provided=equipment_provided,
                av_cost=av_cost,
                technical_support=technical_support,
                setup_time=setup_time,
                contact_emergency=contact_emergency
            )
            av.save()

        elif vendor_type == 'decor':
            design_theme = request.POST.get('design_theme')
            items_supplied = request.POST.get('items_supplied')
            decor_cost = request.POST.get('decor_cost')
            setup_time = request.POST.get('setup_time')
            return_tear_down_time = request.POST.get('return_tear_down_time')

            decor = Decor(
                vendor=vendor,
                design_theme=design_theme,
                items_supplied=items_supplied,
                decor_cost=decor_cost,
                setup_time=setup_time,
                return_tear_down_time=return_tear_down_time
            )
            decor.save()

        elif vendor_type == 'entertainment':
            type_of_entertainment = request.POST.get('type_of_entertainment')
            entertainment_cost = request.POST.get('entertainment_cost')
            performance_duration = request.POST.get('performance_duration')
            special_requirements = request.POST.get('special_requirements', '')

            entertainment = Entertainment(
                vendor=vendor,
                type_of_entertainment=type_of_entertainment,
                entertainment_cost=entertainment_cost,
                performance_duration=performance_duration,
                special_requirements=special_requirements
            )
            entertainment.save()

        elif vendor_type == 'security':
            security_personnel_count = request.POST.get('security_personnel_count')
            security_duties = request.POST.get('security_duties')
            security_cost = request.POST.get('security_cost')
            setup_requirements = request.POST.get('setup_requirements')

            security = Security(
                vendor=vendor,
                security_personnel_count=security_personnel_count,
                security_duties=security_duties,
                security_cost=security_cost,
                setup_requirements=setup_requirements
            )
            security.save()

        elif vendor_type == 'printing':
            printed_materials = request.POST.get('printed_materials')
            printing_cost = request.POST.get('printing_cost')
            design_requirements = request.POST.get('design_requirements')
            delivery_timeframe = request.POST.get('delivery_timeframe')

            printing = Printing(
                vendor=vendor,
                printed_materials=printed_materials,
                printing_cost=printing_cost,
                design_requirements=design_requirements,
                delivery_timeframe=delivery_timeframe
            )
            printing.save()

        elif vendor_type == 'transportation':
            transport_type = request.POST.get('transport_type')
            transportation_cost = request.POST.get('transportation_cost')
            transport_schedule = request.POST.get('transport_schedule')
            passenger_capacity = request.POST.get('passenger_capacity')
            special_requests = request.POST.get('special_requests')

            transportation = Transportation(
                vendor=vendor,
                transport_type=transport_type,
                transportation_cost=transportation_cost,
                transport_schedule=transport_schedule,
                passenger_capacity=passenger_capacity,
                special_requests=special_requests
            )
            transportation.save()

        elif vendor_type == 'waste_management':
            waste_types_collected = request.POST.get('waste_types_collected')
            waste_management_cost = request.POST.get('waste_management_cost')
            service_details = request.POST.get('service_details')
            restroom_facilities = request.POST.get('restroom_facilities')

            waste_management = WasteManagement(
                vendor=vendor,
                waste_types_collected=waste_types_collected,
                waste_management_cost=waste_management_cost,
                service_details=service_details,
                restroom_facilities=restroom_facilities
            )
            waste_management.save()

        # Redirect to a success or vendor listing page
        return redirect('add_vendor')  # Redirect to the page that shows all the vendors

    else:
        # If not POST, just render the form
        user_events = Event.objects.filter(user=request.user)  # Fetch events for the logged-in user
        return render(request, 'add_vendor.html', {'user_events': user_events})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Vendor, Event  # Assuming Event is your event model

@login_required
def view_vendors(request):
    events = Event.objects.filter(user=request.user)  # Get events for the logged-in user
    return render(request, "view_vendors.html", {"events": events})

from django.http import JsonResponse
from .models import Vendor, Venue, Catering, AV, Decor, Entertainment, Security, Printing, Transportation, WasteManagement

def get_vendors(request, event_id):
    try:
        vendors = Vendor.objects.filter(event_id=event_id).select_related(
            "venue", "catering", "av", "decor", "entertainment",
            "security", "printing", "transportation", "wastemanagement"
        )
        vendor_list = []

        for vendor in vendors:
            vendor_data = {
                "vendor_id": vendor.id,
                "name": vendor.name,
                "vendor_type": vendor.vendor_type,
                "description": vendor.description,
                "payment_cost": float(vendor.payment_cost),
                "deposit": float(vendor.deposit),
                "credit_days": vendor.credit_days,
                "payment_status": vendor.payment_status,
            }

            # Add venue-specific fields
            if vendor.vendor_type == "venue" and hasattr(vendor, "venue"):
                vendor_data.update({
                    "venue_address": vendor.venue.venue_address,
                    "venue_booking_time": vendor.venue.venue_booking_time,
                    "venue_requirements": vendor.venue.venue_requirements,
                    "venue_capacity": vendor.venue.venue_capacity,
                    "venue_rental_cost": float(vendor.venue.venue_rental_cost),
                })

            # Add catering-specific fields
            elif vendor.vendor_type == "catering" and hasattr(vendor, "catering"):
                vendor_data.update({
                    "catering_type": vendor.catering.catering_type,
                    "menu_options": vendor.catering.menu_options,
                    "dietary_preferences": vendor.catering.dietary_preferences,
                    "catering_cost": float(vendor.catering.catering_cost),
                    "service_requirements": vendor.catering.service_requirements,
                })

            # Add AV-specific fields
            elif vendor.vendor_type == "av" and hasattr(vendor, "av"):
                vendor_data.update({
                    "equipment_provided": vendor.av.equipment_provided,
                    "av_cost": float(vendor.av.av_cost),
                    "technical_support": vendor.av.technical_support,
                    "setup_time": vendor.av.setup_time,
                    "contact_emergency": vendor.av.contact_emergency,
                })

            # Add decor-specific fields
            elif vendor.vendor_type == "decor" and hasattr(vendor, "decor"):
                vendor_data.update({
                    "design_theme": vendor.decor.design_theme,
                    "items_supplied": vendor.decor.items_supplied,
                    "decor_cost": float(vendor.decor.decor_cost),
                    "setup_time": vendor.decor.setup_time,
                    "return_tear_down_time": vendor.decor.return_tear_down_time,
                })

            # Add entertainment-specific fields
            elif vendor.vendor_type == "entertainment" and hasattr(vendor, "entertainment"):
                vendor_data.update({
                    "type_of_entertainment": vendor.entertainment.type_of_entertainment,
                    "entertainment_cost": float(vendor.entertainment.entertainment_cost),
                    "performance_duration": vendor.entertainment.performance_duration,
                    "special_requirements": vendor.entertainment.special_requirements,
                })

            # Add security-specific fields
            elif vendor.vendor_type == "security" and hasattr(vendor, "security"):
                vendor_data.update({
                    "security_personnel_count": vendor.security.security_personnel_count,
                    "security_duties": vendor.security.security_duties,
                    "security_cost": float(vendor.security.security_cost),
                    "setup_requirements": vendor.security.setup_requirements,
                })

            # Add printing-specific fields
            elif vendor.vendor_type == "printing" and hasattr(vendor, "printing"):
                vendor_data.update({
                    "printed_materials": vendor.printing.printed_materials,
                    "printing_cost": float(vendor.printing.printing_cost),
                    "design_requirements": vendor.printing.design_requirements,
                    "delivery_timeframe": vendor.printing.delivery_timeframe,
                })

            # Add transportation-specific fields
            elif vendor.vendor_type == "transportation" and hasattr(vendor, "transportation"):
                vendor_data.update({
                    "transport_type": vendor.transportation.transport_type,
                    "transportation_cost": float(vendor.transportation.transportation_cost),
                    "transport_schedule": vendor.transportation.transport_schedule,
                    "passenger_capacity": vendor.transportation.passenger_capacity,
                    "special_requests": vendor.transportation.special_requests,
                })

            # Add waste management-specific fields
            elif vendor.vendor_type == "waste_management" and hasattr(vendor, "wastemanagement"):
                vendor_data.update({
                    "waste_types_collected": vendor.wastemanagement.waste_types_collected,
                    "waste_management_cost": float(vendor.wastemanagement.waste_management_cost),
                    "service_details": vendor.wastemanagement.service_details,
                    "restroom_facilities": vendor.wastemanagement.restroom_facilities,
                })

            vendor_list.append(vendor_data)

        return JsonResponse({"vendors": vendor_list}, safe=False)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)




from django.shortcuts import render, redirect
from .models import Ticket, Event
from django.contrib import messages
@login_required
def add_ticket(request):
    if request.method == 'POST':
        event_id = request.POST.get('event')
       
        ticket_type = request.POST.get('ticket_type')
        ticket_description = request.POST.get('ticket_description')
       
        regular_price = request.POST.get('regular_price', None)
        early_bird_price = request.POST.get('early_bird_price', None)
        vip_price = request.POST.get('vip_price', None)
        vvip_price = request.POST.get('vvip_price', None)
        total_quantity = request.POST.get('total_quantity')
        available_quantity = request.POST.get('available_quantity')
        min_quantity = request.POST.get('min_quantity')
        max_quantity = request.POST.get('max_quantity')
        early_bird_expiry_date = request.POST.get('early_bird_expiry_date', None)

        # Convert prices and quantities to the correct data types
      
        early_bird_price = float(early_bird_price) if early_bird_price else None
        regular_price = float(regular_price) if regular_price else None
        vip_price = float(vip_price) if vip_price else None
        vvip_price = float(vvip_price) if vvip_price else None
        total_quantity = int(total_quantity)
        available_quantity = int(available_quantity)
        min_quantity = int(min_quantity)
        max_quantity = int(max_quantity)
        early_bird_expiry_date = early_bird_expiry_date if early_bird_expiry_date else None

        # Get the selected event for the logged-in user
        try:
            event = Event.objects.get(id=event_id, user=request.user)
        except Event.DoesNotExist:
            messages.error(request, "Event not found or you do not have permission to add tickets for this event.")
            return redirect('event_list')  # Redirect to a page with events for the user

        # Create a new ticket
        Ticket.objects.create(
            event=event,
            
            ticket_type=ticket_type,
            ticket_description=ticket_description,
            
            early_bird_price=early_bird_price,
            regular_price=regular_price,
            vip_price=vip_price,
            vvip_price=vvip_price,
            total_quantity=total_quantity,
            available_quantity=available_quantity,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
            early_bird_expiry_date=early_bird_expiry_date
        )

        messages.success(request, 'Ticket added successfully!')
        return redirect('add_ticket')  # Redirect to the ticket list or another page

    # Filter events related to the logged-in user
    events = Event.objects.filter(user=request.user)  # Only show events that belong to the logged-in user
    return render(request, 'add_ticket.html', {'events': events})


@login_required
def view_tickets(request):
    return render(request, 'add_ticket.html')


from django.shortcuts import render, redirect
from .models import Event, EventSchedule
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def add_schedule(request):
    events = Event.objects.filter(user=request.user)  # Filter events for the logged-in user

    if request.method == 'POST':
        session_type = request.POST.get('session_type')
        start_time_str = request.POST.get('start_time')
        end_time_str = request.POST.get('end_time')
        description = request.POST.get('description')
        event_id = request.POST.get('event')

        # Ensure all fields are filled in
        if session_type and start_time_str and end_time_str and description and event_id:
            try:
                # Convert start_time and end_time from strings to datetime objects
                start_time = timezone.datetime.fromisoformat(start_time_str)
                end_time = timezone.datetime.fromisoformat(end_time_str)

                event = Event.objects.get(id=event_id)  # Get the event selected by the user
                EventSchedule.objects.create(
                    event=event,
                    session_type=session_type,
                    start_time=start_time,
                    end_time=end_time,
                    description=description
                )
                return redirect('add_schedule')  # Redirect to the event details page
            except ValueError:
                # If datetime conversion fails
                return render(request, 'add_schedule.html', {'events': events, 'error': 'Invalid datetime format.'})
            except Event.DoesNotExist:
                # Handle case where the event doesn't exist
                return render(request, 'add_schedule.html', {'events': events, 'error': 'Event does not exist.'})
        else:
            # If any field is missing, return an error message
            return render(request, 'add_schedule.html', {'events': events, 'error': 'Please fill in all fields.'})

    return render(request, 'add_schedule.html', {'events': events})



@login_required
def view_schedules(request):
    
    return render(request, 'add_schedule.html')



from django.shortcuts import render, redirect
from .models import Event, Sponsor
from django.contrib.auth.decorators import login_required

@login_required
def add_sponsor(request):
    events = Event.objects.filter(user=request.user)  # Filter events for the logged-in user

    if request.method == 'POST':
        event_id = request.POST.get('event')
        name = request.POST.get('name')
        logo = request.FILES.get('logo')
        description = request.POST.get('description')
        website_url = request.POST.get('website_url')

        # Ensure all required fields are filled
        if event_id and name and logo and description:
            event = Event.objects.get(id=event_id)  # Get the event selected by the user
            
            # Create the sponsor entry
            Sponsor.objects.create(
                event=event,
                name=name,
                logo=logo,
                description=description,
                website_url=website_url
            )

            return redirect('add_sponsor', )  # Redirect to the event details page
        else:
            return render(request, 'add_sponsor.html', {'events': events, 'error': 'Please fill in all required fields.'})

    return render(request, 'add_sponsor.html', {'events': events})


@login_required
def view_sponsors(request):
    
    return render(request, 'add_sponsor.html')


from django.shortcuts import render, redirect
from django.http import JsonResponse
from decimal import Decimal
from .models import Event, Ticket, Attendee
from decimal import Decimal

def add_attendee(request):
    if request.method == 'POST':
        event_id = request.POST.get('event')
        ticket_id = request.POST.get('ticket')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        discount_percentage = request.POST.get('discount_percentage', 0)  # Default to 0 if not provided

        # Ensure all fields are filled
        if event_id and ticket_id and name and email and phone_number:
            event = Event.objects.get(id=event_id)
            ticket = Ticket.objects.get(id=ticket_id)

            # Get the ticket price based on ticket type
            if ticket.ticket_type == 'early_bird':
                ticket_price = ticket.early_bird_price
            elif ticket.ticket_type == 'vip':
                ticket_price = ticket.vip_price
            elif ticket.ticket_type == 'vvip':
                ticket_price = ticket.vvip_price
            else:  # Regular ticket
                ticket_price = ticket.regular_price

            # If ticket price is None, handle it
            if ticket_price is None:
                return JsonResponse({'error': 'Ticket price is not set for this ticket type'}, status=400)

            # Ensure discount percentage is valid (i.e., a float or Decimal)
            try:
                discount_percentage = Decimal(discount_percentage) / 100  # Convert to a decimal fraction
            except (ValueError, TypeError):
                return JsonResponse({'error': 'Invalid discount percentage'}, status=400)

            # Apply discount only if discount_percentage is valid
            final_ticket_price = ticket_price - (ticket_price * discount_percentage)

            # Add the Attendee
            Attendee.objects.create(
                event=event,
                ticket=ticket,
                name=name,
                email=email,
                phone_number=phone_number,
                ticket_price=final_ticket_price  # Store the final price
            )

            return redirect('add_attendee')

    events = Event.objects.all()
    return render(request, 'add_attendee.html', {'events': events})



def get_ticket_types(request):
    event_id = request.GET.get('event_id')
    tickets = Ticket.objects.filter(event_id=event_id).values(
        'id', 'ticket_type', 'early_bird_price', 'vip_price', 'vvip_price', 'regular_price'
    )

    ticket_data = []
    for ticket in tickets:
        # Check which price to display based on ticket type
        if ticket['ticket_type'] == 'early_bird':
            ticket_data.append({
                'id': ticket['id'],
                'ticket_type': ticket['ticket_type'],
                'price': ticket['early_bird_price']
            })
        elif ticket['ticket_type'] == 'vip':
            ticket_data.append({
                'id': ticket['id'],
                'ticket_type': ticket['ticket_type'],
                'price': ticket['vip_price']
            })
        elif ticket['ticket_type'] == 'vvip':
            ticket_data.append({
                'id': ticket['id'],
                'ticket_type': ticket['ticket_type'],
                'price': ticket['vvip_price']
            })
        elif ticket['ticket_type'] == 'regular':
            ticket_data.append({
                'id': ticket['id'],
                'ticket_type': ticket['ticket_type'],
                'price': ticket['regular_price']  # Adding the regular price for regular tickets
            })
        else:
            # Default case for other ticket types
            ticket_data.append({
                'id': ticket['id'],
                'ticket_type': ticket['ticket_type'],
                'price': ticket['early_bird_price']  # Default to early bird price if ticket type is not specified
            })

    return JsonResponse({'tickets': ticket_data})





@login_required
def view_attendees(request):
    return render(request, 'add_attendee.html')


@login_required
def reports(request):


    return render(request, 'reports.html')


@login_required
def profile_settings(request):
    return render(request, 'buywifi/profile_settings.html')

def logout_view(request):
    logout(request)
    return redirect('home')
