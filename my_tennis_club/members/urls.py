from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [    
    
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('api/', views.members_list, name='api'),
    path('api/<int:id>', views.member_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)