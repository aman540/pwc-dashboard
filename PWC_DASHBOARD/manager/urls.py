from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ManagerListView.as_view(), name="manager-list"),
    path('managercreate/', views.ManagerCreateView.as_view(), name="manager-create"),
    path('managerdetail/<str:pk>',
         views.Managerdetail, name="manager-detail"),

    #     path('managerdetail/<str:pk>',
    #          views.ManagerDetailView.as_view(), name="manager-detail"),
    #     path('managerupdate/<str:pk>',
    #          views.ManagerUpdateView.as_view(), name="manager-update"),
    path('managerdelete/<str:pk>',
         views.ManagerDeleteView.as_view(), name="manager-delete"),
    path('update_user/', views.Update_profile, name='update_user'),
]
