from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from venv1.django1.SecureWitness.models import *


class IndexView(generic.ListView):
    template_name = 'SecureWitness/index.html'


class GroupView(generic.ListView):
    model = Group
    template_name = 'SecureWitness/groups.html'