from django.urls import path
from . import views
from . import api_view

urlpatterns = [
    path('professors/', api_view.get_all_professors , name = 'api_professors'),
    path('professor/<str:pk>', api_view.get_by_id , name = 'api_get_by_id'),
    path('professor/new', api_view.new_professor , name = 'api_new_professor'),
    path('professor/update/<str:pk>', api_view.update_professor , name = 'api_update_professor'),
    path('professor/delete/<str:pk>', api_view.delete_professor , name = 'api_delete_professor'),

]
