from django.urls import path
from resume.views import *

app_name = 'resume'

urlpatterns = [
    path('', about_view, name = 'about'),
    path('about/', about_view, name ='about'),
    path('contact/', contact_view, name='contact'),
    path('biography/', biography_view, name='biography'),
    path('languages/', languages_view, name='languages'),
    path('interests/', interests_view, name='interests'),
    path('projects/', projects_view, name='projects'),
    path('skills/', skills_view, name='skills'),
    path('education/', education_view, name='education')
]
