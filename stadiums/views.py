from django.shortcuts import render, get_object_or_404
from datetime import date, datetime, time
from .models import Stadium, Field, Booking


def home(request):
    stadiums = Stadium.objects.filter(is_active=True)

    context = {
        'stadiums': stadiums
    }

    return render(request, 'stadiums/home.html', context)

def field_schedule(request, field_id):
    field = get_object_or_404(
        Field,
        id=field_id,
        is_active=True
    )

    selected_date = request.GET.get('date')

    if selected_date:
        try:
            selected_date = datetime.strptime(
                selected_date,
                '%Y-%m-%d'
            ).date()
        except ValueError:
            selected_date = date.today()
    else:
        selected_date = date.today()

    time_slots = []

    for hour in range(6, 22):
        start = time(hour, 0)
        end = time(hour + 1, 0)

        is_booked = Booking.objects.filter(
            field=field,
            booking_date=selected_date,
            start_time__lt=end,
            end_time__gt=start,
            status__in=['pending', 'confirmed']
        ).exists()

        time_slots.append({
            'start': start,
            'end': end,
            'is_booked': is_booked,
        })

    context = {
        'field': field,
        'selected_date': selected_date,
        'time_slots': time_slots,
    }

    return render(
        request,
        'stadiums/field_schedule.html',
        context
    )

def stadium_detail(request, stadium_id):
    stadium = get_object_or_404(
        Stadium,
        id=stadium_id,
        is_active=True
    )

    fields = stadium.fields.filter(is_active=True)

    context = {
        'stadium': stadium,
        'fields': fields,
    }

    return render(
        request,
        'stadiums/stadium_detail.html',
        context
    )