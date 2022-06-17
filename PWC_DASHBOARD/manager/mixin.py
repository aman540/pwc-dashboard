from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class OrganiserAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organisor"""
# or not request.user.is_organisor .... if no one wants a manager to see other manager

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
