from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='car_images/')
    seating_capacity = models.IntegerField()

    def __str__(self):
        return f"{self.make} {self.model}"



class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  
    start_date = models.DateField()
    end_date = models.DateField()
    timestamp = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"Reservation for {self.car} by {self.customer}"