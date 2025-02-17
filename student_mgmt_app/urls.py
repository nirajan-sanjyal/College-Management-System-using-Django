
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



    path('student_home/', student_home, name="student_home"),
    path('student_view_attendance/', student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave/', student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save/', student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback/', student_feedback, name="student_feedback"),
    path('student_feedback_save/', student_feedback_save, name="student_feedback_save"),
    path('student_profile/', student_profile, name="student_profile"),
    path('student_profile_update/', student_profile_update, name="student_profile_update"),
    path('student_view_result/', student_view_result, name="student_view_result"),

]