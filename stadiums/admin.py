from django.contrib import admin
from .models import Stadium, Field, Booking


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'field_type',
        'price_per_hour',
        'is_active',
        'created_at',
    )

    list_filter = ('field_type', 'is_active')
    search_fields = ('name', 'address')


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'stadium',
        'price_per_hour',
        'is_active',
    )

    list_filter = ('stadium', 'is_active')
    search_fields = ('name', 'stadium__name')
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'field',
        'booking_date',
        'start_time',
        'end_time',
        'total_price',
        'status',
    )

    list_filter = (
        'status',
        'booking_date',
        'field',
    )

    search_fields = (
        'user__username',
        'field__name',
    )