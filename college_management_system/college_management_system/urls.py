"""college_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,HOD_views,Staff_views,Student_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE,name='base'),

    # Login Path
    path('', views.LOGIN, name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    # Logout
    path('doLogout',views.doLogout,name='logout'),

    # Profile Update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),
    # HOD Panel URL
    path('Hod/Home',HOD_views.HOME,name='hod_home'),
    path('Hod/Student/Add',HOD_views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',HOD_views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',HOD_views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',HOD_views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',HOD_views.DELETE_STUDENT,name='delete_student'),

    path('Hod/Staff/Add',HOD_views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',HOD_views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',HOD_views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update/',HOD_views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',HOD_views.DELETE_STAFF,name='delete_staff'),

    path('Hod/Course/Add',HOD_views.ADD_COURSE,name='add_course'),
    path('Hod/Course/View',HOD_views.VIEW_COURSE,name='view_course'),
    path('Hod/Course/Edit/<str:id>',HOD_views.EDIT_COURSE,name='edit_course'),
    path('Hod/Course/Update',HOD_views.UPDATE_COURSE,name='update_course'),
    path('Hod/Course/Delete/<str:id>',HOD_views.DELETE_COURSE,name='delete_course'),
    path('Hod/Subject/Add',HOD_views.ADD_SUBJECT,name='add_subject'),
    path('Hod/Subject/View',HOD_views.VIEW_SUBJECT,name='view_subject'),
    path('Hod/subject/Edit/<str:id>',HOD_views.EDIT_SUBJECT,name='edit_subject'),
    path('Hod/Subject/Update',HOD_views.UPDATE_SUBJECT,name='update_subject'),
    path('Hod/Subject/Delete/<str:id>',HOD_views.DELETE_SUBJECT,name='delete_subject'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
