from django.urls import path
from . import views

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
    path('associatescreate/<str:pk>',
         views.create_associates, name='create_associates'),
    path('associatesget/<str:pk>', views.get_associates, name='get_associates'),
    path('associatesupdate/<str:pk>',
         views.UpdateAssociates, name='update_associates'),
    path('associatesdelete/<str:pk>',
         views.DeleteAssociates, name="associates-delete"),
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
]
