from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import View, TemplateView, DetailView, ListView

from django.template import RequestContext

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group, Permission

from landing.models import *

def index(request):
    return render(request, 'index.html')

class IndexView(ListView):
    model = Sitewide
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['subheadlines_list'] = SubNotes.objects.all()
        context['site'] = Sitewide.objects.all()[0]
        return context
