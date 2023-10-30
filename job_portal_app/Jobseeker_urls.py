from django.urls import path

from job_portal_app.Jobseeker_views import AboutView,ApplicationStatusView,Profile,UpdateProfileView,ViewDetailedProfile, GalleryView, IndexView,JobListView,Single_JobView,ApplyView,Applied_JobView

urlpatterns = [
    
    path('',IndexView.as_view()),
    path('gallerry',GalleryView.as_view()),
    path('viewabout',AboutView.as_view()),
    path('job_list_view',JobListView.as_view()),
    path('single_job_view',Single_JobView.as_view()),
    path('apply',ApplyView.as_view()),
    path('appliedjobview',Applied_JobView.as_view()),
    path('updateprofile',Profile.as_view()),
    path('viewprofile',ViewDetailedProfile.as_view()),
    path('re_updatejprofile',UpdateProfileView.as_view()),
    path('result',ApplicationStatusView.as_view()),
]
def urls():
    return urlpatterns, 'jobseeker','jobseeker'