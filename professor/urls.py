from django.urls import path
from . import views


urlpatterns = [
    path('professors/', views.get_all_professors , name = 'professors'),
    path('professor/<str:pk>', views.get_by_id , name = 'get_by_id'),
    path('professor/new', views.new_professor , name = 'new_professor'),
    path('professor/update/<str:pk>', views.update_professor , name = 'update_professor'),
    path('professor/delete/<str:pk>', views.delete_professor , name = 'delete_professor'),

]
