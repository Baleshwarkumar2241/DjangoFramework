from django.db import models
from django.contrib.auth.models import User, update_last_login
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

STATE_CHOICE = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)

def __str__(self):
    return str(self.id)


CATEGORY_CHOICES = (
    ('P', 'Physician Sp.'),   
    ('D', 'Dentist'),   
    ('N', 'Neurologist'),   
    ('F', 'Family Physicians'),   
)

class DoctorDetails(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    doctor_fees = models.FloatField()    
    discription = models.TextField()   
    doctype = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=5)
    hospital_image = models.ImageField(upload_to='product')

def __str__(self):
    return str(self.id)

# ==============================================================================

class State(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hospitals')

    def __str__(self):
        return self.name
    

class Facility(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False, default="")  

    def __str__(self):
        return self.title

class Availibility(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='availabilies')

    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='availabilies')

    updated_at = models.DateTimeField(auto_now=True)

    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.hospital.name} - {self.facility.title}'