# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from batch.models import Batch

from django.shortcuts import render
from django.http import HttpResponse


django_logger = logging.getLogger("django")


def helloWorld(request):
    return HttpResponse("Hello, world. You're at the batches index.")


class indexView(TemplateView):
    template_name = "index_template.html"
