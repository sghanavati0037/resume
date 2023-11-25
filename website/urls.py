from django.urls import path
from website.views import *

app_name='website'
urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('education', education_view, name='education'),
    path('experience', experience_view, name='experience'),
    path('skills', skills_view, name='skills'),
    path('project', project_view, name='project'),
    path('contact', contact_view, name='contact'),
]
