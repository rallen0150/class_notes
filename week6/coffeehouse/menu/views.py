from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView

from menu.models import Special

class IndexView(ListView):
    template_name = "index.html"
    model = Special

    # Keep this for looking at how this works
    #
    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context['object_list'] = Special.objects.all()
    #     return context

class ProfileView(TemplateView):
    template_name = "profile.html"

class SpecialUpdateView(UpdateView):
    model = Special
    success_url = '/'
    fields = ('title', 'description', 'cost')

    # To prevent other users from editing other information
    def get_queryset(self):
        # Checks to see if the logged in user is the owner
        if self.request.user.profile.is_owner:
            return Special.objects.all()
        # If any other user, then they cannot edit another user's stuff
        return Special.objects.filter(created_by=self.request.user)

class SpecialDeleteView(DeleteView):
    model = Special
    success_url = '/'

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return Special.objects.all()
        return []
