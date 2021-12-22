"""gameweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import viewsTest
from . import test2

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('hello/', viewsTest.hello),
    
    
    
    path('testdb/', test2.testdb),
    path('testdb2/', test2.querydb),
    
    # 统计报表
    path('test_axis_arrow/', viewsTest.test_axis_arrow),
]
