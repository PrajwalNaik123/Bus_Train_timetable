from django.db import models
class Bus(models.Model):
    number=models.CharField(max_length=10)
    bus_type=models.CharField(max_length=20)
    arrival_time=models.TimeField()
    departure_time=models.TimeField()
    reaching_time=models.TimeField()
    start_point=models.CharField(max_length=100)
    destination_point=models.CharField(max_length=100)
    via=models.TextField()
    
class Train(models.Model):
    number=models.CharField(max_length=10)
    train_type=models.CharField(max_length=20)
    arrival_time=models.TimeField()
    departure_time=models.TimeField()
    reaching_time=models.TimeField()
    start_point=models.CharField(max_length=100)
    destination_point=models.CharField(max_length=100)
    via=models.TextField()
    days_of_service = models.CharField(
    max_length=100,
    default="Daily",  
    help_text="e.g. Mon, Tue, Wed or Daily"
)
    def __str__(self):
        return f"{self.number} - {self.start_point} to {self.destination_point}"