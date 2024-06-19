"""
URL configuration for pmarket project.

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
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),  
    
    path('admin/', admin.site.urls),
    path('api/', include('project.urls')),
    path('api/', include('students.urls')),
    path('api/', include('professor.urls')),
    path('api/', include('chat.urls')),
    path('api/token/', TokenObtainPairView.as_view()),

    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),

]

handler404 = 'utils.error_view.handler404'
handler500 = 'utils.error_view.handler500'
