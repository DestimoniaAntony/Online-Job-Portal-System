from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from job_portal_app.models import Book, Employer, Job, Jobseeker, JobseekerProfile

class IndexView(TemplateView):
    template_name = "employer/index.html"
    
class AboutView(TemplateView):
    template_name = "employer/about.html"
    
class GalleryView(TemplateView):
    template_name = "employer/gallery.html"
    
class PostJobView(TemplateView):
    template_name = "employer/post-job.html"
    
    def post(self, request, *args, **kwargs):
        re = Employer.objects.get(user_id=self.request.user.id)
        
        image = request.FILES['image']
        ob=FileSystemStorage()
        obj=ob.save(image.name, image)
        email = request.POST['email']
        title = request.POST['title']
        location = request.POST['location']
        job_type = request.POST['job_type']
        description = request.POST['description']
        companyname = request.POST['companyname']
        company_description = request.POST['company_description']
        website = request.POST['website']
        fb_username = request.POST['fb_username']
        tw_username = request.POST['tw_username']
        lk_username = request.POST['lk_username']
        logo = request.FILES['logo']
        log=ob.save(logo.name, logo)
        published_on=request.POST['published_on']
        vacancy=request.POST['vacancy']
        experience=request.POST['experience']
        salary=request.POST['salary']
        last_date=request.POST['last_date']
        gender=request.POST['gender']
        
        reg = Job()
        
        reg.employer_id = re.id
        reg.image=obj 
        reg.email = email       
        reg.title = title
        reg.location = location
        reg.job_type = job_type
        reg.description = description
        reg.companyname = companyname
        reg.company_description = company_description
        reg.website = website
        reg.fb_username = fb_username
        reg.tw_username = tw_username
        reg.lk_username = lk_username
        reg.logo = log
        reg.published_on = published_on 
        reg.vacancy = vacancy 
        reg.experience = experience 
        reg.salary = salary 
        reg.last_date = last_date  
        reg.gender = gender

        reg.save()
        return render(request, 'employer/index.html', {'message': "Successfully applied"})

class JobListView(TemplateView):
    template_name = "employer/view_jobs_vacancies.html"
    
    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        id1=Employer.objects.get(user_id=self.request.user.id)
        jobs = Job.objects.filter(employer_id=id1.id)
        context['jobs'] = jobs
        return context
    
class AppliedJobVacancyView(TemplateView):
    template_name = "employer/applied_posts.html"
    
    def get_context_data(self, **kwargs):
        context = super(AppliedJobVacancyView, self).get_context_data(**kwargs)
        id2=Employer.objects.get(user_id=self.request.user.id)
        bookings = Book.objects.filter(job_id=id2.id,status="Applied")
        context['bookings'] = bookings
        return context
    
class RejectView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Book.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})
    
class UpdateJobVacancyView(TemplateView):
    template_name = "employer/update_job.html"        
    def get_context_data(self, **kwargs):
        context = super(UpdateJobVacancyView, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        bookings = Job.objects.get(id=id3)
        context['f'] = bookings
        return context
    
    def post(self, request, *args, **kwargs):
        re = Employer.objects.get(user_id=self.request.user.id)
        id3 = request.GET['id']
        email = request.POST['email']
        title = request.POST['title']
        location = request.POST['location']
        job_type = request.POST['job_type']
        description = request.POST['description']
        companyname = request.POST['companyname']
        company_description = request.POST['company_description']
        website = request.POST['website']
        fb_username = request.POST['fb_username']
        tw_username = request.POST['tw_username']
        lk_username = request.POST['lk_username']
        vacancy=request.POST['vacancy']
        experience=request.POST['experience']
        salary=request.POST['salary']
        last_date=request.POST['last_date']
        
        reg = Job.objects.get(id=id3)
        reg.employer_id = re.id
        reg.email = email       
        reg.title = title
        reg.location = location
        reg.job_type = job_type
        reg.description = description
        reg.companyname = companyname
        reg.company_description = company_description
        reg.website = website
        reg.fb_username = fb_username
        reg.tw_username = tw_username
        reg.lk_username = lk_username
        reg.vacancy = vacancy 
        reg.experience = experience 
        reg.salary = salary 
        reg.last_date = last_date  

        reg.save()
        return render(request, 'employer/index.html', {'message': "Successfully applied"})
    
class ViewDetailedProfile(TemplateView):
    template_name = "employer/detailed_candidate_view.html"
    
    def get_context_data(self, **kwargs):
        context = super(ViewDetailedProfile, self).get_context_data(**kwargs)
        id2 = self.request.GET['id']
        id=Jobseeker.objects.get(id=id2)
        profile = JobseekerProfile.objects.filter(jobseeker_id=id)
        context['profile'] = profile
        return context

class AproveView(View):
    def dispatch(self,request,*args,**kwargs):
        id2 = self.request.GET['id']
        book=Book.objects.get(pk=id2)
        
        book.status = "Selected"
        book.save()
        return render(request, 'employer/index.html', {'message': "Candidate selected for interview"})
    