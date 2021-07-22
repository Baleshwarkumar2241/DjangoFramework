from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Availibility, Patient, DoctorDetails, Facility, State, City, Hospital
from .forms import CustomerRegistrationForm, CustomerProfileForm, AddDoctorsForm
from django.contrib import messages
from django.db.models import Q


#=====================Home_Page =================================================

# def home(request):
#     return render(request, 'app/home.html')
class DoctorView(View):
    def get(self, request):
        physician = DoctorDetails.objects.filter(category='P')
        dentist = DoctorDetails.objects.filter(category='D')
        return render(request, 'app/home.html', {'physician':physician, 'dentist':dentist})

#=====================Product-details_Page=======================================

class DoctorDetailView(View):
    def get(self, request, pk):
        product = DoctorDetails.objects.get(pk=pk)
        return render(request, 'app/productdetails.html', {'product':product})


#=================AddDoctorProfile=========================================================

class AddDoctorProfileView(View):
    def get(self, request):
        form = AddDoctorsForm()
        return render(request, 'app/adddoctor.html', {'form':form ,'active':'btn-primary'})
    def post(self, request):
        form = AddDoctorsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            name = form.cleaned_data['name']
            doctor_fees = form.cleaned_data['doctor_fees']
            discription = form.cleaned_data['discription']
            doctype = form.cleaned_data['doctype']
            category = form.cleaned_data['category']
            hospital_image = form.cleaned_data['hospital_image']
            reg = DoctorDetails(title=title, name=name, doctor_fees=doctor_fees, discription=discription, doctype=doctype, category=category, hospital_image=hospital_image)
            reg.save()
            messages.success(request, 'Congratulation !! Profile Update Successfully!')
        return render(request, 'app/adddoctor.html', {'form':form, 'active':'btn-primary'})
    



#===============================Profile_Page=================================================

# def profile(request):
#     return render(request, 'app/profile.html')
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Patient(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Added Doctor!! Successfully!')
        return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})





#===================================address_Page==============================================

def address(request):
    add = Patient.objects.filter(user=request.user)
    return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})




#===================================Order_Page=====================================================

def orders(request):
    return render(request, 'app/orders.html')


#====================================ChangePassord_Page==============================================

# def change_password(request):
#     return render(request, 'app/changepassword.html')


#======================================Physician_Page=================================================

def physician(request, data=None):
    if data == None:
        physician = DoctorDetails.objects.filter(category='P')
    elif data == 'medical' or data == 'medical':
        physician = DoctorDetails.objects.filter(category='P').filter(doctype=data)
    elif data == 'below':
        physician = DoctorDetails.objects.filter(category='P').filter(doctor_fees__lt=10000)        
    elif data == 'above':
        physician = DoctorDetails.objects.filter(category='P').filter(doctor_fees__gt=10000)        
    return render(request, 'app/physician.html', {'physician': physician})



#==============================Dentist Page==============================================================    
def dentist(request, data=None):
    if data == None:
        dentist = DoctorDetails.objects.filter(category='D')
    elif data == 'medical' or data == 'medical':
        dentist = DoctorDetails.objects.filter(category='D').filter(doctype=data)
    elif data == 'below':
        dentist = DoctorDetails.objects.filter(category='D').filter(doctor_fees__lt=10000)        
    elif data == 'above':
        dentist = DoctorDetails.objects.filter(category='D').filter(doctor_fees__gt=10000)        
    return render(request, 'app/dentist.html', {'dentist': dentist})




#=====================================Login_Page===========================================================

# def login(request):
#     return render(request, 'app/login.html')



#===============================Customerregistration_Page===================================================

# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! Registered Successfully')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})


#====================Search==========================================================================

def search1(request):
    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    selected_facility_id = request.GET.get('facility')
    facilities = Facility.objects.all().order_by('pk')
    if selected_state_id:
        cities = City.objects.filter(state=selected_state_id)
    else:
        cities = City.objects.all() 

    states = State.objects.all()
    hospitals = Hospital.objects.all()

    if selected_city_id:
        hospitals = hospitals.filter(city=City(pk=selected_city_id))

    if selected_facility_id:
        availities = Availibility.objects.all()
        if selected_city_id:
            availities = availities.filter(hospital__city=City(pk=selected_city_id))
            
        availities = availities.filter(facility=Facility(pk=selected_facility_id), available__gt=0)

        hospitals = []
        for ava in availities:
            hospitals.append(ava.hospital)
        print("Hospitals", hospitals)        

    context = {
        'facilities' : facilities,
        'states' : states,
        'cities' : cities,
        'hospitals' : hospitals,
        'selected_state_id' : selected_state_id,
        'selected_city_id' : selected_city_id,
        'selected_facility_id' : selected_facility_id,

    }
    return render(request, 'app/search.html', context=context)

# ====================Search Doctor============================================================================

class AllDoctorsDetailView(View):
    def get(self, request):
        if 'q' in request.GET:
            q = request.GET['q']
            multiSearch = (Q(title__icontains=q) | Q(doctype__icontains=q))
            allDoctors = DoctorDetails.objects.filter(multiSearch)
        else:    
            allDoctors = DoctorDetails.objects.all()


        if 'q' in request.GET:
            q = request.GET['q']
            multiSearch = (Q(address__icontains=q) | Q(name__icontains=q))
            allHospitals = Hospital.objects.filter(multiSearch)
        else:    
            allHospitals = Hospital.objects.all()


         

        context1 = {
            'allHospitals':allHospitals,
            'allDoctors':allDoctors,

        }

        return render(request, 'app/search1.html', context1)

#=========================================================================================================

class AdminPanelView(View):
    def get(self, request):
        context = { 'admin1' : 'active' }
        return render(request, 'app/admin.html', context)


#==============================================================================
        
# class AdminDashoardView(View):
#     def get(self, request):
#         return render(request, 'app/admindashboard.html')