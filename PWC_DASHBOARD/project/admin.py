from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Project)
admin.site.register(Status)
admin.site.register(UserProfile)
admin.site.register(Manager)
admin.site.register(Associates)
admin.site.register(Associate)
admin.site.register(Project_Associate)

admin.site.register(Phase)
admin.site.register(Technology)
admin.site.register(Technoproject)
admin.site.register(PhaseDurationOfProject)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']
