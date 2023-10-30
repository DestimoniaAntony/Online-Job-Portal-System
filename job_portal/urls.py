"""
URL configuration for job_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from job_portal_app import Employer_urls, Jobseeker_urls, admin_urls

from job_portal_app.views import IndexView,JobseekerRegView,EmployerRegView,loginview,AboutView,GalleryView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',IndexView.as_view()),
    path('gallery',GalleryView.as_view()),
    path('aboutview',AboutView.as_view()),
    path('jobseekerReg',JobseekerRegView.as_view()),
    path('employerReg',EmployerRegView.as_view()),
    path('loginview',loginview.as_view()),
    path('jobseeker/',Jobseeker_urls.urls()),
    path('employer/',Employer_urls.urls()),
    path('admin/',admin_urls.urls())
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
