from django.contrib import admin
from tickets.models import *

admin.site.register(SessionFormat)
admin.site.register(Session)
admin.site.register(Booking)
admin.site.register(Orders)
admin.site.register(TicketType)
admin.site.register(Ticket)
