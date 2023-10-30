from django.urls import path

from job_portal_app.admin_views import RemoveCandidateView,RemoveJobPostView,AboutView, GalleryView, IndexView,EmployerRequestView,JobseekerRequestView,ApproveView,RejectView,JobListView,AppliedJobVacancyView


urlpatterns = [
    path('',IndexView.as_view()),
    path('gallery',GalleryView.as_view()),
    path('aboutview',AboutView.as_view()),
    path('employer_request',EmployerRequestView.as_view()),
    path('jobseeker_request',JobseekerRequestView.as_view()),
    path('aprove',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('job_list',JobListView.as_view()),
    path('applied_job_list',AppliedJobVacancyView.as_view()),
    path('removecandidate',RemoveCandidateView.as_view()),
    path('removejobpost',RemoveJobPostView.as_view())
]
def urls():
    return urlpatterns, 'admin','admin'