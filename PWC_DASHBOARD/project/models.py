from pyexpat import model
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=100, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organistation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


class Project(models.Model):

    title = models.CharField(max_length=200, null=False, blank=True)
    description = models.TextField(null=False, blank=True)
    client = models.CharField(max_length=50, null=False, blank=True)
    from_duration = models.DateField(null=True, blank=True)
    to_duration = models.DateField(null=True, blank=True)
    # phase = models.CharField(max_length=50, null=False, blank=True)
    # source=models.CharField(choices=SOURCE_CHOICE,max_length=100)
    organistation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    status = models.ForeignKey(
        "Status", related_name="projects", on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.title
# employee


class Associates(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False, blank=True)
    email = models.EmailField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name
# phase


class Phase(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Status(models.Model):
    # imformation,test,dev,pwd,aws,.....
    name = models.CharField(max_length=50)
    # organistation=models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Technoproject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    associates = models.ForeignKey(Associates, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.project.title + ":" + self.associates.name + ":" + self.technology.name


class PhaseDurationOfProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)
    # organistation=models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return (self.project.title)+" -- "+self.phase.name+" -- " + str(self.from_date)+" -- "+str(self.to_date)
