# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from batch.models import Batch

django_logger = logging.getLogger("django")


class indexView(TemplateView):
    template_name = "batch.html"
    # model = Batch
    context_object_name = "info"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # msg = "Welcome to the home of the Passata"
        # context_data.update({"msg": msg})
        return context_data
