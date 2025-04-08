from django.shortcuts import render

# Create your views here.
def attendee_home(request):    
    return render(request, 'att_home.html')


from django.shortcuts import render, get_object_or_404
from organizers.models import Attendee, Event


def attendee_home(request):
    # Query all events from the database
    events = Event.objects.all()
    
    # Loop through the events and fetch the regular ticket price for each
    event_details = []
    for event in events:
        # Fetch the regular ticket price for each event
        regular_ticket = event.tickets.filter(ticket_type='regular').first()
        ticket_price = regular_ticket.regular_price if regular_ticket else 0.00
        event_details.append({
            'event': event,
            'ticket_price': ticket_price
        })
    
    return render(request, 'att_home.html', {'event_details': event_details})

import json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from organizers.models import Event, Ticket, Order
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum



@csrf_exempt
def ticket_buying_page(request, event_id):
    # Fetch the event based on the event_id
    event = get_object_or_404(Event, id=event_id)
    
    # Fetch the tickets related to this event
    tickets = Ticket.objects.filter(event=event)
    
    for ticket in tickets:
        # Calculate the number of tickets already bought
        total_quantity = Order.objects.filter(ticket=ticket).aggregate(Sum('ticket_quantity'))['ticket_quantity__sum'] or 0
        
        # Calculate the available quantity by subtracting the number of purchased tickets
        ticket.available_quantity = ticket.total_quantity - total_quantity
        
        # Ensure that available quantity does not exceed the maximum quantity per user
        ticket.max_quantity = ticket.max_quantity  # Keep the max quantity unchanged, used in the frontend for validation
        
        # Pick the correct ticket price based on the ticket type
        if ticket.ticket_type == 'early_bird':
            ticket.ticket_price = ticket.early_bird_price
        elif ticket.ticket_type == 'regular':
            ticket.ticket_price = ticket.regular_price
        elif ticket.ticket_type == 'vip':
            ticket.ticket_price = ticket.vip_price
        elif ticket.ticket_type == 'vvip':
            ticket.ticket_price = ticket.vvip_price

    return render(request, 'ticket_buying_page.html', {'event': event, 'tickets': tickets})


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from organizers.models import Event, Ticket, Order, Attendee
import json

@csrf_exempt
def submit_ticket_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            event_id = data.get('event_id')
            ticket_id = data.get('ticket_id')
            event = get_object_or_404(Event, id=event_id)
            ticket = get_object_or_404(Ticket, id=ticket_id)

            attendee_name = data.get('attendee_name')
            attendee_email = data.get('attendee_email')
            attendee_phone = data.get('attendee_phone')
            payment_method = data.get('payment_method')
            ticket_quantity = int(data.get('ticket_quantity'))
            total_price = float(data.get('total_price'))

            # Save order
            order = Order.objects.create(
                event=event,
                ticket=ticket,
                attendee_name=attendee_name,
                attendee_email=attendee_email,
                attendee_phone=attendee_phone,
                payment_method=payment_method,
                ticket_quantity=ticket_quantity,
                total_price=total_price
            )

            # Save attendee
            Attendee.objects.create(
                event=event,
                ticket=ticket,
                name=attendee_name,
                email=attendee_email,
                phone_number=attendee_phone,
                ticket_price=total_price,
            )

            organizer_email = event.user.email if event.user else settings.DEFAULT_FROM_EMAIL

            context = {
                'attendee_name': attendee_name,
                'event_name': event.event_name,
                'ticket_type': ticket.ticket_type,
                'ticket_quantity': ticket_quantity,
                'total_price': total_price,
                'payment_method': payment_method,
                'attendee_phone': attendee_phone,
                'event_date': event.event_date.strftime('%B %d, %Y, %I:%M %p'),
                'organizer_email': organizer_email,
            }

            # Render HTML email body
            email_subject = f"Your Ticket for {event.event_name}"
            email_body = render_to_string('ticket_email_template.html', context)

            # Send HTML email
            email = EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=organizer_email,
                to=[attendee_email],
            )
            email.content_subtype = 'html'  # Important to send as HTML
            email.send(fail_silently=False)

            return JsonResponse({
                'success': True,
                'message': 'Ticket purchased successfully! The ticket has been sent to your email.'
            })

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data received'})
        except ValueError as e:
            return JsonResponse({'success': False, 'message': f'Value error: {str(e)}'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})



# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactMessage  # A model to store contact messages, if necessary

# View to display the contact form
def contact_page(request):
    return render(request, 'att_contact.html')

# View to handle form submission
def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Optionally, save the contact message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)

        # Redirect or send a response after submission
        return HttpResponse("Thank you for contacting us! We will get back to you soon.")

    return redirect('contact_page')

