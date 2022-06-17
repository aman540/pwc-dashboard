from urllib import request
from django.shortcuts import redirect, render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from project.models import *
from .forms import*
from .mixin import OrganiserAndLoginRequiredMixin
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import random
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def Update_profile(request):
    user = request.user
    form = Updateuser(instance=user)
    if request.method == 'POST':
        form = Updateuser(request.POST, request.FILES, instance=user)

        if form.is_valid():
            print(form.data)
            form.save()
            return redirect('manager-list')
    context = {
        'form': form
    }
    return render(request, 'update-user.html', context)


@login_required(login_url='login')
def Managerdetail(request, pk):
    user = request.user
    manager = Manager.objects.get(id=pk)
    c = str(user) == str(manager)

    context = {'manager': manager, "c": c

               }
    return render(request, 'managerdetail.html', context)


class ManagerListView(OrganiserAndLoginRequiredMixin, generic.ListView):
    template_name = "managerlist.html"

    def get_queryset(self):
        if self.request.user.is_organisor:
            # print(self.request.user.id)
            return Manager.objects.filter(organistation=self.request.user.userprofile)
        else:
            my_p = Manager.objects.get(user=self.request.user)
            organistation = my_p.organistation
            # print(organistation)
            # (organistation=organistation)
            return Manager.objects.filter(organistation=organistation)


class ManagerCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = "managercreate.html"
    form_class = ManagerForm

    def get_success_url(self):

        return reverse("manager-list")

    def form_valid(self, form):
        print("a")
        user = form.save(commit=False)
        user.is_manager = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Manager.objects.create(
            user=user, organistation=self.request.user.userprofile)
        html_content = f'''
            <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
                <div style="margin:50px auto;width:80%;padding:20px 0">
                    <div style="border-bottom:1px solid #eee">
                    <a href="" style="font-size:1.4em;color: #46c894;text-decoration:none;font-weight:600">PWC</a>
                    </div>
                    <p style="font-size:1.1em">Hi,.</p>
                    <p>You have been added as a manager  with user id {user.email} . </p>
<p><a href="http://127.0.0.1:8000/reset-password/">Click here to reset your password.</a></p>
                    <p>Use your email-  and reset your password.</p>

                    <p style="font-size:0.9em;">Thank You</p>
                    <hr style="border:none;border-top:1.5px solid #eee" />
                </div>
            </div>
            '''
        mail = EmailMessage(
            'PwC',
            html_content,
            None,
            [user.email],

        )
        mail.content_subtype = "html"
        mail.send()

        # send_mail(
        #     subject="you are invited to be an agent",
        #     message="You were added as an agent on CRM plese login to start working .Your login credintial are username="+user.username+" and password="+user.password,
        #     from_email="admin@admin.com",
        #     recipient_list=['user.email']
        # )

        # agent.organistation=self.request.user.userprofile
        # agent.save()
        return super(ManagerCreateView, self).form_valid(form)


# class ManagerDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
#     template_name = "managerdetail.html"

#     def get_queryset(self):

#         m = Manager.objects.all()

#         return m


# class ManagerUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
#     template_name = "managerupdate.html"
#     form_class = ManagerForm

#     def get_success_url(self):
#         return reverse('manager-list')

#     def get_queryset(self):
#         organistation = self.request.user.userprofile
#         return Manager.objects.filter(organistation=organistation)


class ManagerDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = "manager_confirm_delete.html"
    a = 0

    def get_queryset(self):
        if self.request.user.is_organisor:
            organistation = self.request.user.userprofile
            return Manager.objects.filter(organistation=organistation)
        else:
            self.a = 1
            manager = self.request.user

            return Manager.objects.filter(user=manager)

    def get_success_url(self):
        if self.a == 1:
            return reverse("logout")
        else:
            return reverse("manager-list")
