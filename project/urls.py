from django.urls import path
from . import views


urlpatterns = [
    #path('/', views. , name = 'home'),
    path('projects/', views.get_all_projects , name = 'projects'),
    path('project/<str:pk>', views.get_by_id , name = 'get_by_id'),
    path('project/new', views.new_project , name = 'new_project'),
    path('project/update/<str:pk>', views.update_project , name = 'update_project'),
    path('project/delete/<str:pk>', views.delete_project , name = 'delete_project'),

    path('<str:pk>/reviews', views.add_review , name = 'add_review'),
    path('<str:pk>/reviews/delete', views.delete_review , name = 'delete_review'),

]
