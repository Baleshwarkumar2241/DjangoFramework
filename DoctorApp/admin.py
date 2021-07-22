from django.contrib import admin

from .models import (
    Facility,
    Patient,
    DoctorDetails,
    State,
    City,
    Hospital,
    Availibility,

    
)
from django.db.models.signals import post_save
from django.dispatch import receiver

# Register your models here.

@admin.register(Patient)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']


    
@admin.register(DoctorDetails)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name', 'doctor_fees', 'discription', 'doctype', 'category', 'hospital_image']


# =================================================================================================================

@receiver(post_save, sender=Hospital)
def afterHospitialSave(signal, instance, **kwargs):
   Facilities = Facility.objects.all()
   for facility in Facilities:
       availibility = Availibility(hospital=instance, facility=facility)
       availibility.save()


@receiver(post_save, sender=Facility)
def afterFacilitySave(signal, instance, **kwargs):
   hospitals = Hospital.objects.all()
   for hospital in hospitals:
       availibility = Availibility(hospital=hospital, facility=instance)
       availibility.save()


class FacilityAdmin(admin.ModelAdmin):
    model = Facility
    list_display = ['title'] 
    


class HospitalAdmin(admin.ModelAdmin):
    model = Hospital
    list_display = ['name', 'phone', 'address', 'city']




class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ['name','state']


class AvailibilityAdmin(admin.ModelAdmin):
    model = Availibility
    list_display = ['hospital','facility','total','available', 'updated_at']
    list_editable = ['total', 'available']


admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Availibility, AvailibilityAdmin)











