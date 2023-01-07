# vaccination/test.py

from django.test import TestCase

from .models import VaccinationCenter, VaccinationDosage, Appointment

class VaccinationCenterTestCase(TestCase):
    def setUp(self):
        VaccinationCenter.objects.create(name="Vaccination Center 1", location="Location 1", capacity=100)
        VaccinationCenter.objects.create(name="Vaccination Center 2", location="Location 2", capacity=200)

    def test_vaccination_center_str(self):
        center1 = VaccinationCenter.objects.get(name="Vaccination Center 1")
        center2 = VaccinationCenter.objects.get(name="Vaccination Center 2")
        self.assertEqual(str(center1), "Vaccination Center 1")
        self.assertEqual(str(center2), "Vaccination Center 2")

class VaccinationDosageTestCase(TestCase):
    def setUp(self):
        center1 = VaccinationCenter.objects.create(name="Vaccination Center 1", location="Location 1", capacity=100)
        center2 = VaccinationCenter.objects.create(name="Vaccination Center 2", location="Location 2", capacity=200)
        VaccinationDosage.objects.create(vaccination_center=center1, vaccine="Vaccine 1", date="2022-01-01", time="09:00:00")
        VaccinationDosage.objects.create(vaccination_center=center2, vaccine="Vaccine 2", date="2022-01-02", time="10:00:00")

    def test_vaccination_dosage_str(self):
        dosage1 = VaccinationDosage.objects.get(vaccine="Vaccine 1")
        dosage2 = VaccinationDosage.objects.get(vaccine="Vaccine 2")
        self.assertEqual(str(dosage1), "Vaccine 1 at Vaccination Center 1 on 2022-01-01 at 09:00:00")
        self.assertEqual(str(dosage2), "Vaccine 2 at Vaccination Center 2 on 2022-01-02 at 10:00:00")

class AppointmentTestCase(TestCase):
    def setUp(self):
        center1 = VaccinationCenter.objects.create(name="Vaccination Center 1", location="Location 1", capacity=100)
        center2 = VaccinationCenter.objects.create(name="Vaccination Center 2", location="Location 2", capacity=200)
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        Appointment.objects.create(user=user1, vaccination_center=center1, date="2022-01-01", time="09:00:00")
        Appointment.objects.create(user=user2, vaccination_center=center2, date="2022-01-02", time="10:00:00")

    def test_appointment_str(self):
        appointment1 = Appointment.objects.get(user__username="user1")
        appointment2 = Appointment.objects.get(user__username="user2")
        self.assertEqual(str(appointment1), "user1 at Vaccination Center 1 on 2022-01-01 at 09:00:00")
        self.assertEqual(str(appointment2), "user2 at Vaccination Center 2 on 2022-01-02 at 10:00:00")

if __name__ == "__main__":
    TestCase.main()
