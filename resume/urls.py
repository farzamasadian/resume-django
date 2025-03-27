from django.urls import path
from resume.views import *

app_name = 'resume'

urlpatterns = [
    path('', index_view, name = 'index'),
    path('#contact/', contact_view, name='contact'),
    path('#biography/', biography_view, name='biography'),
    path('#languages/', languages_view, name='languages'),
    path('#interests/', interests_view, name='interests'),
    path('#projects/', projects_view, name='projects'),
]
