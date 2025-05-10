from django.contrib import admin
from .models import Bus, Train

# Bus Admin Customization
class BusAdmin(admin.ModelAdmin):
    list_display = ('number', 'bus_type', 'start_point', 'destination_point', 'arrival_time', 'departure_time', 'reaching_time', 'via')
    search_fields = ('number', 'start_point', 'destination_point')
    list_filter = ('bus_type',)

# Train Admin Customization
class TrainAdmin(admin.ModelAdmin):
    list_display = ('number', 'train_type', 'start_point', 'destination_point', 'arrival_time', 'departure_time', 'reaching_time', 'via','days_of_service')
    search_fields = ('number', 'start_point', 'destination_point')
    list_filter = ('train_type',)

# Register the models with the admin
admin.site.register(Bus, BusAdmin)
admin.site.register(Train, TrainAdmin)
