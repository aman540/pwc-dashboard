from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [

    # The home page
    path('', views.index, name='dashboard'),
    path('graph', views.graph, name='graph'),
    path('projectcreate/', views.create_project, name='create_project'),
    path('project_list/', views.ProjectListview.as_view(), name="project-list"),
    path('projectupdate/<str:pk>',
         views.ProjectUpdateView.as_view(), name="project-update"),
    path('projectdetail/<str:pk>', views.ProjectDetail, name="project-detail"),
    path('projectdelete/<str:pk>',
         views.ProjectDeleteView.as_view(), name="project-delete"),
    # associate
    #     path('associatescreate/<str:pk>',
    #          views.create_associates, name='create_associates'),
    path('associatesget/<str:pk>', views.get_associates, name='get_associates'),



    path('assign_associates/<str:pk>',
         views.assign_associates, name='assign_associates'),
    path('projectassociatesdelete/<str:pk>',
         views.delete_project_associates, name="project-associates-delete"),
    path('associates_list/', views.associates_list, name='associates-list'),
    path('associatesdetail/<str:pk>',
         views.associates_detail, name="associates-detail"),
    path('associates_create/', views.associates_create, name='associates-create'),
    path('associatesupdate/<str:pk>',
         views.associates_update, name='associates-update'),

    path('associatesdelete/<str:pk>',
         views.associates_delete, name="associates-delete"),
    # technology

    path('technologyadd/<str:pk>', views.add_Technology, name='add_technology'),
    path('technologydelete/<str:pk>',
         views.DeleteTechnology, name="technology-delete"),
    path('technologyget/<str:pk>', views.get_technology, name='get_technology'),
    # status update of project
    path('status_update/<str:pk>',
         views.ProjectStatusUpdateView.as_view(), name='status-update'),

    path('phasedurationadd/<str:pk>',
         views.add_phase_duration, name='add_phase_duration'),
    path('phase_duration_get/<str:pk>',
         views.get_phase_duration, name='get_phase_duration'),
    path('phase_duration_update/<str:pk>',
         views.UpdatePhase, name='update_phase_duration'),
    path('phase_duration_delete/<str:pk>',
         views.DeletePhase, name='delete_phase_duration'),
    # Matches any html file
    # password reset,login,signup
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
