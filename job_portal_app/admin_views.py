from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from job_portal_app.models import Book, Employer, Job, Jobseeker

class IndexView(TemplateView):
    template_name = "admin/index.html"
    
class AboutView(TemplateView):
    template_name = "admin/about.html"
    
class GalleryView(TemplateView):
    template_name = "admin/gallery.html"
    
class EmployerRequestView(TemplateView):
    template_name = "admin/employer_request.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmployerRequestView, self).get_context_data(**kwargs)        
        employer = Employer.objects.filter(
            user__last_name='0', user__is_staff='0')
        context['employer'] = employer
        return context
    
class JobseekerRequestView(TemplateView):
    template_name = "admin/jobseeker_request.html"
    
    def get_context_data(self, **kwargs):
        context = super(JobseekerRequestView, self).get_context_data(**kwargs)        
        jobseeker = Jobseeker.objects.filter(
            user__last_name='0', user__is_staff='0')
        context['jobseeker'] = jobseeker
        return context
    
class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = self.request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return render(request, 'admin/index.html', {'message': " Account Approved"})


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '2'
        user.is_active = '0'
        user.save()
        return render(request, 'admin/index.html', {'message': "Account Rejected"})

class JobListView(TemplateView):
    template_name = "admin/view_jobs.html"
    
    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        
        jobs = Job.objects.all()
        context['jobs'] = jobs
        return context
    
class AppliedJobVacancyView(TemplateView):
    template_name = "admin/applied_posts.html"
    
    def get_context_data(self, **kwargs):
        context = super(AppliedJobVacancyView, self).get_context_data(**kwargs)
        
        bookings = Book.objects.filter(status="Applied")
        context['bookings'] = bookings
        return context
    
class RemoveCandidateView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Book.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Candidate Rejected"})
    
class RemoveJobPostView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        Job.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Candidate Rejected"})