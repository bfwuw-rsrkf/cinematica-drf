from django.contrib import admin
from movies.models import *


admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(RoomSize)
admin.site.register(Room)
admin.site.register(Seat)
