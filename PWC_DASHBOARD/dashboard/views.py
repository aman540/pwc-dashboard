from datetime import date
from datetime import datetime
from multiprocessing import context, managers
from pydoc import cli
from django.shortcuts import render, redirect, reverse
from project.models import*
from project.forms import*
from django.contrib.auth.mixins import LoginRequiredMixin
from manager.mixin import OrganiserAndLoginRequiredMixin
from django.views import generic
from django.views.generic import TemplateView, DeleteView, ListView, UpdateView
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.forms import inlineformset_factory

import json

from django.utils.safestring import mark_safe
date_format = "%m/%d/%Y"


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


@ login_required(login_url='login')
def graph(request):
    user = request.user
    green = Status.objects.get(name="Green")
    amber = Status.objects.get(name="Amber")
    red = Status.objects.get(name="Red")

    if request.user.is_organisor:
        # status start
        allmanager = Manager.objects.filter(
            organistation=request.user.userprofile)
        allproject = Project.objects.filter(
            organistation=user.userprofile, manager__isnull=False).order_by("-created").order_by("-created")
        green_status = Project.objects.filter(
            organistation=request.user.userprofile, status=green).count()
        red_status = Project.objects.filter(
            organistation=request.user.userprofile, status=red).count()
        amber_status = Project.objects.filter(
            organistation=request.user.userprofile, status=amber).count()
        none_status = Project.objects.filter(
            organistation=request.user.userprofile, status=None).count()
    elif request.user.is_manager:
        o = Manager.objects.get(user=request.user)
        # status start
        allmanager = Manager.objects.filter(organistation=o.organistation)
        allproject = Project.objects.filter(
            organistation=user.manager.organistation, manager__isnull=False).order_by("-created")
        # filter for agent that is logged in
        allproject = allproject.filter(manager__user=user).order_by("-created")
        green_status = Project.objects.filter(
            manager=o, status=green).count()
        red_status = Project.objects.filter(
            manager=o, status=red).count()
        amber_status = Project.objects.filter(
            manager=o, status=amber).count()
        none_status = Project.objects.filter(
            manager=o, status=None).count()
    t_project_associates = set()
    t_project_duration = set()
    for i in allproject:
        b = Associates.objects.filter(project=i).count()
        t_project_associates.add((i, b))
        if i.from_duration != None:
            a = i.from_duration
            b = i.to_duration
            delta = b-a
            t_project_duration.add((i, delta.days))
        else:
            t_project_duration.add((i, 0))
    t_manager_project = set()
    for i in allmanager:
        b = Project.objects.filter(manager=i)
        t_manager_project.add((i.user.email, b.count()))
    print(t_manager_project)
    context = {'green_status': mark_safe(json.dumps(green_status)), 'red_status': mark_safe(json.dumps(red_status)),
               'amber_status': mark_safe(json.dumps(amber_status)), 'none_status': mark_safe(json.dumps(none_status)),  't_project':  t_project_associates,   't_duration': t_project_duration, 't_manager_project': t_manager_project}
    return render(request, 'home/charts-morris.html', context)


@ login_required(login_url='login')
def index(request):
    user = request.user
    # status

    # all stats
    countorganisers = UserProfile.objects.all().count()
    countmanagers = Manager.objects.all().count()
    countprojects = Project.objects.all().count()
    if request.user.is_organisor:
        # status start
        allmanager = Manager.objects.filter(
            organistation=request.user.userprofile).order_by("-created")
        allproject = Project.objects.filter(
            organistation=user.userprofile, manager__isnull=False).order_by("-created")
        type_erp = Project.objects.filter(
            organistation=user.userprofile, manager__isnull=False, type="Erp").order_by("-created")
        type_aws = Project.objects.filter(
            organistation=user.userprofile, manager__isnull=False, type="aws").order_by("-created")
        type_azure = Project.objects.filter(
            organistation=user.userprofile, manager__isnull=False, type="Azure").order_by("-created")
        type_salesforce = Project.objects.filter(
            organistation=user.userprofile, manager__isnull=False, type="salesforce").order_by("-created")

        Associatesunder_every_project = Associates.objects.all().count()
    elif request.user.is_manager:
        o = Manager.objects.get(user=request.user)
        allmanager = Manager.objects.filter(
            organistation=o.organistation).order_by("-created")

        Associatesunder_every_project = Associates.objects.filter(
            manager=o).count()
        allproject = Project.objects.filter(
            organistation=user.manager.organistation, manager__isnull=False).order_by("-created")
        # filter for agent that is logged in
        allproject = allproject.filter(manager__user=user).order_by("-created")
        type_erp = allproject.filter(type="Erp").order_by("-created")
        type_aws = allproject.filter(type="aws").order_by("-created")
        type_azure = allproject.filter(type="Aws").order_by("-created")
        type_salesforce = allproject.filter(
            type="salesforce").order_by("-created")
        print(type_erp)
    projectcount = allproject.count()
    context = {'co': countorganisers, 'cm': countmanagers,
               'cp': countprojects, 'allproject': allproject, 'allmanager': allmanager, 'pc': projectcount, 'ta': Associatesunder_every_project, "type_erp": type_erp, "type_aws": type_aws, "type_salesforce": type_salesforce, "type_azure": type_azure}

    return render(request, 'home/index.html', context)

# project items


@ login_required(login_url='login')
def create_project(request):

    # If the person_id is not valid, don't go forward.
    # return a 404 instead.

    # manager = request.user
    my_p = Manager.objects.get(user=request.user)
    project_form = Projectforms(request.POST or None)
    # print(project_form.data)
    # if request.method == "POST":
    #     title = request.POST.get("title")
    #     client = request.POST.get("client")
    #     description = request.POST.get("description")
    #     from_duration = request.POST.get("from_duration")
    #     to_duration = request.POST.get("to_duration")
    #     project = Project.objects.create(
    #         manager=my_p,
    #         organistation=my_p.organistation,
    #         title=title,
    #         client=client,
    #         description=description,
    #         from_duration=from_duration,
    #         to_duration=to_duration,
    #         type=type,

    #     )
    if project_form.is_valid():
        new_project = project_form.save(commit=False)
        new_project.title = request.POST.get('title')
        new_project.client = request.POST.get('client')
        new_project.description = request.POST.get('description')
        new_project.from_duration = request.POST.get('from_duration')
        new_project.to_duration = request.POST.get('to_duration')
        new_project.manager = my_p
        new_project.organistation = my_p.organistation
        new_project.save()

        return redirect('create_associates', new_project.id)

    return render(request, 'home/projectcreate.html', {'form': project_form})


class ProjectListview(LoginRequiredMixin, ListView):
    template_name = "home/all_project_list.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Project.objects.filter(
                organistation=user.userprofile, manager__isnull=False).order_by("-created")
        else:
            queryset = Project.objects.filter(
                organistation=user.manager.organistation, manager__isnull=False).order_by("-created")
            # filter for agent that is logged in
            queryset = queryset.filter(manager__user=user).order_by("-created")

        for project in queryset:
            today = date.today()
            p_d = project.to_duration
            delta = p_d - today
            print(delta.days)
            amber = Status.objects.get(name="Amber")
            red = Status.objects.get(name="Red")
            if delta.days < 0 and delta.days >= -7:
                project.status = amber
                project.save()
            elif delta.days < -7:
                project.status = red
                project.save()
        return queryset


@ login_required(login_url='login')
def ProjectDetail(request, pk):
    project = Project.objects.get(id=pk)

    # associates = project.project_associates_set.all()
    associate = Project_Associate.objects.filter(project=project)
    phasedurationofproject = project.phasedurationofproject_set.all()
    a = set()
    for i in phasedurationofproject:
        delta = (i.to_date-i.from_date)
        a.add((i.phase.name, int(delta.days)))
    context = {'project': project, "associates": associate,
               'phasedurationofproject': phasedurationofproject, 'a': a}
    return render(request, 'home/project_detail.html', context)

# Associates


# @ login_required(login_url='login')
# def create_associates(request, pk):
#     user = request.user
#     manager = Manager.objects.get(user=user)
#     project = Project.objects.get(id=pk)
#     if request.method == 'POST':

#         new_associate = Associates.objects.create(
#             project=project, manager=manager, name=request.POST.get(
#                 'name'),
#             email=request.POST.get('email'),
#             designation=request.POST.get('designation'))

#         return redirect('add_technology', pk=new_associate.id)

#     context = {}
#     return render(request, 'associates/associates_create.html', context)


# @ login_required(login_url='login')
# def UpdateAssociates(request, pk):
#     associates = Associates.objects.get(id=pk)
#     project = associates.project
#     form = Associatesforms(instance=associates)

#     if request.user != associates.project.manager.user:
#         return HttpResponse('Virus')
#     if request.method == "POST":
#         form = Associatesforms(
#             request.POST, request.FILES, instance=associates)
#         if form.is_valid():
#             form.save()
#             return redirect('get_associates', pk=project.id)
#     context = {
#         'form': form
#     }
#     return render(request, 'associates/associates_update.html', context)


# @ login_required(login_url='login')
# def DeleteAssociates(request, pk):
#     associate = Associates.objects.get(id=pk)
#     project = Project.objects.get(associates=associate)
#     if request.user != associate.manager.user:
#         return HttpResponse('Virus')

#     if request.method == 'POST':
#         associate.delete()
#         return redirect('get_associates', project.id)
#     return render(request, 'associates/delete.html', {'obj': associate})


@ login_required(login_url='login')
def add_Technology(request, pk):
    user = request.user
    manager = Manager.objects.get(user=user)
    associate = Associates.objects.get(id=pk)
    project = Project.objects.get(associates=associate)
    Techno = TechnologyForm(initial={'associates': associate})
    technology_data = Technology.objects.all()
    if request.method == "POST":
        technology_names = request.POST.getlist('technology')
        for technology_name in technology_names:
            technology, created = Technology.objects.get_or_create(
                name=technology_name)
            Technoproject.objects.create(
                manager=manager,
                project=project,
                associates=associate,
                technology=technology
            )
        return redirect('get_technology', pk=associate.id)
    context = {'form': Techno, 'technology_data': technology_data}
    return render(request, 'technology/technology_add.html', context)


@ login_required(login_url='login')
def DeleteTechnology(request, pk):
    technology = Technoproject.objects.get(id=pk)
    associate = Associates.objects.get(technoproject=technology)
    t = technology.technology
    if request.user != associate.manager.user:
        return HttpResponse('Virus')
    if request.method == 'POST':
        technology.delete()
        return redirect('get_technology', associate.id)
    return render(request, 'technology/delete.html', {'obj': t})


@ login_required(login_url='login')
def get_technology(request, pk):
    associates = Associates.objects.get(id=pk)
    e = Technoproject.objects.filter(
        associates=associates)
    context = {"e": e, "associates": associates}
    return render(request, 'technology/technology_data.html', context)


class ProjectStatusUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "project/project_status_update.html"
    form_class = ProjectStatusUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Project.objects.filter(
                organistation=user.userprofile).order_by("-id")
        else:
            queryset = Project.objects.filter(
                organistation=user.manager.organistation).order_by("-id")
            # filter for agent that is logged in
            queryset = queryset.filter(manager__user=user)
        return queryset

    def get_success_url(self):
        return reverse("project-list")

# phase


@ login_required(login_url='login')
def add_phase_duration(request, pk):
    project = Project.objects.get(id=pk)
    phase_form = PhaseDurationForm(request.POST or None)
    if phase_form.is_valid():
        new_phase = phase_form.save(commit=False)  # Don't save it yet
        new_phase.project = project
        new_phase.save()  # Now save it
        return redirect('get_phase_duration', project.id)
    context = {'form': phase_form, }
    return render(request, 'phase_duration/phase_duration_add.html', context)


@ login_required(login_url='login')
def get_phase_duration(request, pk):
    project = Project.objects.get(id=pk)
    phase_duration = PhaseDurationOfProject.objects.filter(project=project)
    context = {'phase_duration': phase_duration, 'project': project}
    return render(request, 'phase_duration/phase_duration_get.html', context)


@ login_required(login_url='login')
def UpdatePhase(request, pk):
    phase = PhaseDurationOfProject.objects.get(id=pk)
    form = PhaseDurationForm(instance=phase)

    if request.user != phase.project.manager.user:
        return HttpResponse('Virus')
    if request.method == "POST":
        form = PhaseDurationForm(request.POST, request.FILES, instance=phase)
        if form.is_valid():
            form.save()
            return redirect('get_phase_duration', pk=phase.project.id)
    context = {
        'form': form
    }
    return render(request, 'phase_duration/phase_duration_update.html', context)


@ login_required(login_url='login')
def DeletePhase(request, pk):
    phase = PhaseDurationOfProject.objects.get(id=pk)

    if request.user != phase.project.manager.user:
        return HttpResponse('Virus')

    if request.method == 'POST':
        phase.delete()
        return redirect('get_phase_duration', pk=phase.project.id)
    return render(request, 'phase_duration/delete.html', {'obj': phase})


class ProjectUpdateView(OrganiserAndLoginRequiredMixin, UpdateView):
    template_name = "project/projectupdate.html"
    form_class = ProjectUpdateforms

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            return Project.objects.filter(organistation=user.userprofile).order_by("-id")
        else:
            my_p = Manager.objects.get(user=self.request.user)
            return Project.objects.filter(manager=my_p).order_by("-id")
        # user = self.request.user
        # return Project.objects.filter(organistation=user.userprofile).order_by("-id")

    def get_success_url(self):
        return reverse("project-list")


class ProjectDeleteView(OrganiserAndLoginRequiredMixin, DeleteView):
    def get_queryset(self):
        if self.request.user.is_organisor:
            return Project.objects.filter(organistation=self.request.user.id).order_by("-id")
        elif self.request.user.is_manager:
            my_p = Manager.objects.get(user=self.request.user)
            return Project.objects.filter(manager=my_p).order_by("-id")

    def get_success_url(self):
        return reverse("project-list")


# project associate
@ login_required(login_url='login')
def get_associates(request, pk):
    project = Project.objects.get(id=pk)
    e = Project_Associate.objects.filter(
        project=project)
    # techno = e.technoproject_set.all()
    context = {"e": e, "project": project, }
    return render(request, 'project_associates/associates_data.html', context)


@ login_required(login_url='login')
def delete_project_associates(request, pk):
    project_associate = Project_Associate.objects.get(id=pk)
    project = project_associate.project
    a = project_associate.associate
    if request.method == 'POST':
        b = Associate.objects.get(id=a.id)
        b.occupency = b.occupency-1
        b.save()
        project_associate.delete()
        return redirect('get_associates', pk=project.id)
    return render(request, 'project_associates/delete.html', {'obj': project_associate})


@ login_required(login_url='login')
def assign_associates(request, pk):
    project = Project.objects.get(id=pk)
    associate_form = AssignAssociatesforms(request.POST or None)

    if associate_form.is_valid():
        a = associate_form.cleaned_data['associate']
        b = Associate.objects.get(id=a.id)
        b.occupency = b.occupency+1
        b.save()

        new_phase = associate_form.save(commit=False)  # Don't save it yet
        new_phase.project = project
        new_phase.save()  # Now save it
        return redirect('get_associates', project.id)
    # print(new_phase.data)
    context = {'form': associate_form, }
    return render(request, 'project_associates/assign_associate.html', context)

# assocites


@ login_required(login_url='login')
def associates_list(request):
    associate = Associate.objects.all()
    context = {"associate": associate}
    return render(request, 'associates/associates_list.html', context)


@ login_required(login_url='login')
def associates_create(request):
    form = CreateAssociatesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('associates-list')
    context = {"form": form}
    return render(request, 'associates/associates_create.html', context)


@ login_required(login_url='login')
def associates_detail(request, pk):
    associate = Associate.objects.get(id=pk)
    a = associate.project_associate_set.all()

    context = {"associate": associate, "a": a}
    return render(request, 'associates/associates_detail.html', context)


@ login_required(login_url='login')
def associates_delete(request, pk):
    associate = Associate.objects.get(id=pk)
    # if request.user.is_manager:
    #     return HttpResponse('Virus')
    if request.method == 'POST':
        associate.delete()
        return redirect('associates-list')
    return render(request, 'associates/delete.html', {'obj': associate})


@ login_required(login_url='login')
def associates_update(request, pk):
    associates = Associate.objects.get(id=pk)
    form = CreateAssociatesForm(instance=associates)
    # if request.user.is_manager:
    #     return HttpResponse('Virus')
    if request.method == "POST":
        form = Associatesforms(
            request.POST, request.FILES, instance=associates)
        if form.is_valid():
            form.save()
            return redirect('associates-list')
    context = {'form': form}
    return render(request, 'associates/associates_update.html', context)
