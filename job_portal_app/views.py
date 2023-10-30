from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView

from job_portal_app.models import Employer, Jobseeker, UserType
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    
class AboutView(TemplateView):
    template_name = "about.html"
class GalleryView(TemplateView):
    template_name = "gallery.html"
class JobseekerRegView(TemplateView):
    template_name = "jobseekerReg.html"

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'jobseekerReg.html', {'message': "already added the username or email"})

        else:
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='0')
            user.save()
            reg = Jobseeker()
            reg.user = user
            reg.mobile = mobile    
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "jobseeker"
            usertype.save()

            return render(request, 'index.html', {'message': "Jobseeker added successfully"})
    
class EmployerRegView(TemplateView):
    template_name = "EmployerReg.html"

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'EmployerReg.html', {'message': "already added the username or email"})

        else:
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='0')
            user.save()
            reg = Employer()
            reg.user = user
            reg.mobile = mobile    
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "employer"
            usertype.save()

            return render(request, 'index.html', {'message': "Employer added successfully"})
        
class loginview(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "jobseeker":
                    return redirect('/jobseeker')
                elif UserType.objects.get(user_id=user.id).type == "employer":
                    return redirect('/employer')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'login.html', {'message': "Invalid Username or Password"})       
        