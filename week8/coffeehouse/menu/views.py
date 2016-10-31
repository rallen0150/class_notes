from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from menu.models import Special

class SpecialListView(ListView):
    model = Special

class SpecialCreateView(CreateView):
    model = Special
    fields = ('title', 'description')
    success_url = reverse_lazy("special_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)
