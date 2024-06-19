from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.get_all_students , name = 'students'),
    path('student/<str:pk>', views.get_by_id , name = 'get_by_id'),
    path('student/new', views.new_student , name = 'new_student'),
    path('student/update/<str:pk>', views.update_student , name = 'update_student'),
    path('student/delete/<str:pk>', views.delete_student , name = 'delete_student'),

]
