from django.urls import path
from django.views.generic.base import View
from DoctorApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MypasswordChangeForm, MyPasswordResetForm, MySetPasswordForm


urlpatterns = [
    # path('', views.home),
    path('', views.DoctorView.as_view(), name="home"),

#======================================================================================
    path('product-detail/<int:pk>', views.DoctorDetailView.as_view(), name="product-detail"),


#==========================================================================================   

    path('search1/', views.search1, name="search1"),

#======================================================================================    
    path('profile/', views.ProfileView.as_view(), name='profile'),


#======================================================================================  
    path('adddoctor/',views.AddDoctorProfileView.as_view(), name="adddoctor"),
   
#======================================================================================    
    path('address/', views.address, name='address'),

#======================================================================================    
    path('orders/', views.orders, name='orders'),

#===================ChangePassword=====================================================
#   path('changepassword/', views.change_password, name='changepassword'),

    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MypasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),    

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name="passwordchangedone"),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complate/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset__confirm.html'), name='password_reset_confirm'),
    

#==============Login========================================================================    
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

#==============Logout=====================================================================

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name="logout"),

#======================================================================================    
    path('physician/', views.physician, name='physician'),
    path('physician/<slug:data>', views.physician, name='pysiciandata'),


#======================================================================================    
    path('dentist/', views.dentist, name='dentist'),
    path('dentist/<slug:data>', views.dentist, name='dentistdata'),


#======================================================================================    
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),



#=====================================================================================
    path('search/', views.AllDoctorsDetailView.as_view(), name="search"),

#=========================================================================================    

    path('admin1/', views.AdminPanelView.as_view(), name="admin1"),

#===========================================================================================

    # path('admindashboard/', views.AdminDashoardView.as_view(), name="admindashboard")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
