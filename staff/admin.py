from django.contrib import admin
from .models import Staff, Client, Facility, Reservation, Payment

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'role', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('role', 'created_at')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('date_joined',)

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity', 'available')
    search_fields = ('name',)
    list_filter = ('available',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('client', 'facility', 'date', 'time_slot')
    search_fields = ('client__first_name', 'client__last_name', 'facility__name', 'date')
    list_filter = ('date', 'facility')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'payment_date', 'status')
    search_fields = ('client__first_name', 'client__last_name', 'amount')
    list_filter = ('status', 'payment_date')