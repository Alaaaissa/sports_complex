from django.db import models

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50, choices=[
        ('admin', 'Admin'),
        ('trainer', 'Trainer'),
        ('receptionist', 'Receptionist'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Temporarily nullable
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.client.first_name} - {self.facility.name} at {self.date}"

class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ])

    def __str__(self):
        return f"{self.client.first_name} - {self.amount} ({self.status})"