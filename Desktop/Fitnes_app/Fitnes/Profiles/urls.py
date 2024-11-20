from django.urls import path
from . import views
import Expertise.views as expertise

urlpatterns = [
    path('caloryprofile/edit/', views.calory_profile_edit, name='calory_profile_edit'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile', views.profile, name='profile'),
    path('expert/create/', views.create_expert_profile, name='create_expert_profile'),
    path('expert/<int:pk>/edit/', views.edit_expert_profile, name='edit_expert_profile'),
    path('expert/<int:pk>/', views.view_expert_profile, name='view_expert_profile'),
    path('timetables/', expertise.expert_timetable_list, name='timetable_list'),
]
