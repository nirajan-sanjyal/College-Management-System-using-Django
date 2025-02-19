
from django.urls import path

from student_mgmt_app import views
from student_mgmt_app.Student.Studentviews import *

from student_mgmt_app.staff.staffviews import *

urlpatterns = [

    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginUser, name="login"),
    path('logout_user', views.logout_user, name="logout_user"),
    path('registration', views.registration, name="registration"),
    path('doLogin', views.doLogin, name="doLogin"),
    path('doRegistration', views.doRegistration, name="doRegistration"),


 # student_views
    path('student_home/', student_home, name="student_home"),
   


    # staff_views
    path('staff_home/', staff_home, name='staff_home'),
    path('take_attendance/', staff_take_attendance, name='take_attendance'),

]