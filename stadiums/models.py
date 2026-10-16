from django.db import models
from django.contrib.auth.models import User

class Stadium(models.Model):
    FIELD_TYPES = [
        ('5', 'Sân 5 người'),
        ('7', 'Sân 7 người'),
        ('11', 'Sân 11 người'),
    ]

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)

    field_type = models.CharField(
        max_length=10,
        choices=FIELD_TYPES
    )

    price_per_hour = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Field(models.Model):
    stadium = models.ForeignKey(
        Stadium,
        on_delete=models.CASCADE,
        related_name='fields'
    )

    name = models.CharField(max_length=100)

    price_per_hour = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.stadium.name} - {self.name}"



class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ xác nhận'),
        ('confirmed', 'Đã xác nhận'),
        ('cancelled', 'Đã hủy'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    field = models.ForeignKey(
        Field,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    booking_date = models.DateField()

    start_time = models.TimeField()
    end_time = models.TimeField()

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.field.name} - "
            f"{self.booking_date} "
            f"{self.start_time}"
        )