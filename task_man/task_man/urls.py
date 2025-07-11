"""task_man URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.http import HttpResponseRedirect

# Rest API
from rest_framework import routers
from mtasks.serializers import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)



urlpatterns = [
  #  url(r'^$', lambda r: HttpResponseRedirect('admin/')),  
    
    url(r'^advanced_filters/', include('advanced_filters.urls')),
    url(r'^api/v1/', include(router.urls)),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
   # path('', include('templates.accounts'))
]

admin.site.site_header = settings.SITE_HEADER

