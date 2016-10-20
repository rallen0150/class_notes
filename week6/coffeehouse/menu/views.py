from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView

from menu.models import Special, Profile
from django.urls import reverse_lazy

class IndexView(ListView):
    template_name = "index.html"
    model = Special

    # Keep this for looking at how this works
    #
    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context['object_list'] = Special.objects.all()
    #     return context

class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    fields = ('access_level', )
    success_url = reverse_lazy('profile_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user)

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
