#
# fashion/views.py
#
# Default Page generator
#
#
from django.views.generic import View, TemplateView, DetailView, ListView

from django.template import RequestContext

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group, Permission

from .models import News


class FrontPageList(ListView):
    model = News

class NewsDetail(DetailView):
    model = News
    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        this = kwargs['object']
        context['headline_collections'] = Collection.public_objects.filter(news=True, headline__isnull=False).order_by('-dateline')[0:10]
        context['latest_collections'] = Collection.public_objects.order_by('-dateline')[0:20]
        context['collection_list'] = Collection.public_objects.filter(week=this).order_by('slug')

        return context
