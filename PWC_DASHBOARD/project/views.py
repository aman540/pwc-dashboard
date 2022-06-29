from pydoc import cli
from django.shortcuts import render, redirect, reverse
from . models import*
from . forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from manager.mixin import OrganiserAndLoginRequiredMixin
from django.views import generic
from django.views.generic import TemplateView, DeleteView, ListView, UpdateView
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


# class ProjectCreateView(OrganiserAndLoginRequiredMixin, CreateView):
#     template_name = "projectcreate.html"
#     form_class = Projectforms

#     def get_success_url(self):
#         return reverse("home")

# def form_valid(self, form):
#     send_mail(
#         subject="A lead has been created",
#         message="Go to site to see the new lead",
#         from_email="test@test.com",
#         recipient_list=['test2@test.com,']

#     )
# return super(ProjectCreateView, self).form_valid(form)


# @login_required(login_url='login')
# def add_Technology(request, pk):
#     user = request.user
#     manager = Manager.objects.get(user=user)
#     associate = Associates.objects.get(id=pk)
#     project = Project.objects.get(associates=associate)

#     Techno = Technologyforms(request.POST or None)
#     if Techno.is_valid():
#         new_techno = Techno.save(commit=False)  # Don't save it yet
#         new_techno.manager = manager
#         new_techno.associates = associate
#         new_techno.project = project
#         new_techno.save()  # Now save it
#         return redirect('get_technology', pk=associate.id)

#     context = {'form': Techno}
#     return render(request, 'technology_add.html', context)

# technology


# phase


# Associates
