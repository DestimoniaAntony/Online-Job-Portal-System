from django.urls import path

from job_portal_app.Employer_views import AproveView,AboutView, GalleryView,ViewDetailedProfile, IndexView,PostJobView,JobListView,AppliedJobVacancyView,RejectView,UpdateJobVacancyView

urlpatterns = [
    
    path('',IndexView.as_view()),
    path('gallery',GalleryView.as_view()),
    path('aboutview',AboutView.as_view()),
    path('post_job',PostJobView.as_view()),
    path('job_list',JobListView.as_view()),
    path('applied_job_list',AppliedJobVacancyView.as_view()),
    path('removed',RejectView.as_view()),
    path('update_job_vacancy',UpdateJobVacancyView.as_view()),
    path('detailedcandidateview',ViewDetailedProfile.as_view()),
    path('aproveview',AproveView.as_view())
]
def urls():
    return urlpatterns, 'employer','employer'