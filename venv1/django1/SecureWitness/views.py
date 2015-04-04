from django.shortcuts import render_to_response, render
from django.views import generic
from django.http import HttpResponseRedirect

from SecureWitness.models import *


class GroupIndexView(generic.ListView):
    template_name = 'SecureWitness/group_index.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return the last five published groups."""
        return Group.objects.order_by('-GID')[:5]


class GroupView(generic.DetailView):
    model = Group
    template_name = 'SecureWitness/group_detail.html'