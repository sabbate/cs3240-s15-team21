from django.shortcuts import render_to_response
from django.views import generic

from SecureWitness.models import Group


class GroupIndexView(generic.ListView):
    template_name = 'SecureWitness/group_index.html'

    def get_queryset(self):
        """Return the last five published groups."""
        return Group.objects.order_by('-GID')[:5]


class GroupView(generic.ListView):
    template_name = 'SecureWitness/group.html'
    context_object_name = 'group_list'

    def get_queryset(self):
        """Return last five groups"""
        return Group.objects.order_by('-GID')[:5]