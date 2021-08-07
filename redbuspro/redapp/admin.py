from django.contrib import admin
from .models import Ticket_User

# Register your models here.
@admin.register(Ticket_User)
class ticketAdmin(admin.ModelAdmin):
    list_display = ['name']