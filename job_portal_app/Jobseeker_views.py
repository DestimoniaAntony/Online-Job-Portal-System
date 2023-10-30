from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from job_portal_app.models import Book, Job, Jobseeker, JobseekerProfile

class AboutView(TemplateView):
    template_name = "jobseeker/about.html"
    
class GalleryView(TemplateView):
    template_name = "jobseeker/gallery.html"
    
class IndexView(TemplateView):
    template_name = "jobseeker/index.html"
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        
        jobs = Job.objects.all()
        context['jobs'] = jobs
        return context
    
    def post(self, request, *args, **kwargs):
        
        search = self.request.POST['search']
        jobs = Job.objects.filter(title__icontains=search)
        
        return render(request,'jobseeker/view_jobs.html',{'jobs':jobs})
class JobListView(TemplateView):
    template_name = "jobseeker/view_jobs.html"
    
    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        
        jobs = Job.objects.all()
        context['jobs'] = jobs
        return context
    
    def post(self, request, *args, **kwargs):
        
        search = self.request.POST['search']
        jobs = Job.objects.filter(title__icontains=search)
        # ,companyname__icontains=search
        return render(request,'jobseeker/view_jobs.html',{'jobs':jobs})
    
class Single_JobView(TemplateView):
    template_name = "jobseeker/detailed_jobview.html"
    
    def get_context_data(self, **kwargs):
        context = super(Single_JobView, self).get_context_data(**kwargs)
        id1 = self.request.GET['id']
        single_job = Job.objects.get(id=id1)
        context['single_job'] = single_job
        return context

class ApplyView(View):
    def dispatch(self,request,*args,**kwargs):
        id1 = request.GET['id']
        usid=Jobseeker.objects.get(user_id=self.request.user.id)
        
        ca = Book()
        
        ca.job_id=id1
        ca.jobseeker_id = usid.id
        ca.status = "Applied"
        ca.save()
        return render(request, 'jobseeker/index.html', {'message': "You have successfully applied for this job. Once your application is being processed our team will contact you. Kindly wait for the further notifications."})
    
class Applied_JobView(TemplateView):
    template_name = "jobseeker/applied_jobview.html"
    
    def get_context_data(self, **kwargs):
        context = super(Applied_JobView, self).get_context_data(**kwargs)
        id2=Jobseeker.objects.get(user_id=self.request.user.id)
        applied_job = Book.objects.filter(jobseeker_id=id2.id)
        context['applied_job'] = applied_job
        return context

class Profile(TemplateView):
    template_name = "jobseeker/profile.html"
    def post(self, request, *args, **kwargs):
        re = Jobseeker.objects.get(user_id=self.request.user.id)
        
        image = request.FILES['image']
        ob=FileSystemStorage()
        obj=ob.save(image.name, image)
        age = request.POST['age']
        gender = request.POST['gender']
        qualification = request.POST['qualification']
        address = request.POST['address']
        pincode = request.POST['pincode']
        experience = request.POST['experience']
        skills = request.POST['skills']
        resume = request.FILES['resume']
        resume=ob.save(resume.name, resume)
        
        reg = JobseekerProfile()
        
        reg.jobseeker_id = re.id
        reg.image=obj 
        reg.age = age       
        reg.gender = gender
        reg.qualification = qualification
        reg.address = address
        reg.pincode = pincode
        reg.experience = experience
        reg.skills = skills
        reg.resume = resume
        reg.save()
        return render(request, 'jobseeker/index.html', {'message': "Successfully profile updated"})
class ViewDetailedProfile(TemplateView):
    template_name = "jobseeker/view_profile.html"
    
    def get_context_data(self, **kwargs):
        context = super(ViewDetailedProfile, self).get_context_data(**kwargs)
        id2=Jobseeker.objects.get(user_id=self.request.user.id)
        profile = JobseekerProfile.objects.filter(jobseeker_id=id2.id)
        context['profile'] = profile
        return context
    
class UpdateProfileView(TemplateView):
    template_name = "jobseeker/updateprofile.html"        
    def get_context_data(self, **kwargs):
        context = super(UpdateProfileView, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = JobseekerProfile.objects.get(id=id3)
        context['f'] = pro
        return context
    def post(self, request, *args, **kwargs):
        re = Jobseeker.objects.get(user_id=self.request.user.id)
        id3 = request.GET['id']
        age = request.POST['age']
        gender = request.POST['gender']
        qualification = request.POST['qualification']
        address = request.POST['address']
        pincode = request.POST['pincode']
        experience = request.POST['experience']
        skills = request.POST['skills']
        
        reg = JobseekerProfile.objects.get(id=id3)
        
        reg.jobseeker_id = re.id
        reg.age = age       
        reg.gender = gender
        reg.qualification = qualification
        reg.address = address
        reg.pincode = pincode
        reg.experience = experience
        reg.skills = skills
        reg.save()
        return render(request, 'jobseeker/index.html', {'message': "Successfully profile updated"})
    
class ApplicationStatusView(TemplateView):
    template_name = "jobseeker/application_result.html" 
    
    def get_context_data(self, **kwargs):
        context = super(ApplicationStatusView, self).get_context_data(**kwargs)
        id2=Jobseeker.objects.get(user_id=self.request.user.id)
        applied_job = Book.objects.filter(jobseeker_id=id2.id, status="Selected")
        context['applied_job'] = applied_job
        return context