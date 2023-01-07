from django.db import models

class Center(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()


class Appointment(models.Model):
    name = models.CharField(max_length=100, default='Default name')
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    date = models.DateField()

    def is_full(self):
        appointments = Appointment.objects.filter(center=self)
        if appointments.count() >= self.capacity:
            return True
        return False

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, default='Default name')


class VaccinationCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Vaccination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccination_center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE)
    date = models.DateField()
