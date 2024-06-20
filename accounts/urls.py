from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('sign_up', views.signup , name = 'sign_up'),  
    path('profile', views.profile , name = 'profile'), 
    path('profile_edit', views.profile_edit , name = 'profile_edit'), 
    path('register/', views.register , name = 'register'),
    path('userinfo/', views.current_user , name = 'user_info'),  
    path('userinfo/update/', views.update_user , name = 'update_user'),  
    path('forgot_password/', views.forgot_password , name = 'forgot_password'),  
    path('reset_password/<str:token>', views.reset_password , name = 'reset_password'),  

    

]
