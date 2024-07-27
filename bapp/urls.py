"""
URL configuration for bapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bapp1.views import index
from bapp1.views import register
from bapp1.views import profile
#from bapp1.views import register_submit

from bapp1.views import success_view
from bapp1.views import update_view
from bapp1.views import Donor_profile_view
from bapp1.views import Seeker_profile_view
from bapp1.views import dashboard_view
from bapp1.views import update_profile, edit_profile
from bapp1.views import delete_profile
# from bapp1.views import search_blood




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('index/register', register, name='register'),
    path('index/profile', profile , name='profile'),
    # path('index/register/', register_submit, name='register'),
    path('index/success/', success_view, name='success'),
    path('index/update/', update_view, name='update'),
    path('index/Donor_profile/',Donor_profile_view, name='Donor_profile' ),
    path('index/seeker_profile/',Seeker_profile_view, name='seeker_profile'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('index/edit/<int:id>/', edit_profile, name='edit_profile'),
    path('index/update/<int:pk>/', update_profile, name='update_profile'),
    path('index/delete/<int:id>/', delete_profile, name='delete_profile'),
    # path('search/',search_blood, name='search_blood'),
]

