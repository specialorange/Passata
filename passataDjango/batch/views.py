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


def index(request):
    return HttpResponse("Hello, world. You're at the batches index.")


class indexView(TemplateView):
    template_name = "batch.html"
    # model = Batch
    context_object_name = "info"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        msg = "Welcome to the home of the Passata"
        context_data.update({"msg": msg})
        return context_data


class BatchesView(ListView):
    template_name = "batches.html"
    model = Batch
    context_object_name = "batches"

    def get_queryset(self, **kwargs):
        qs = (
            Batch.objects.select_related(
                "recipe",
                "volume_unit",
            )
            .prefetch_related(
                "step",
            )
            .filter()
            .order_by("createdAt")
        )
        # breakpoint()
        return qs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({})
        return context_data


class BatchView(DetailView):
    template_name = "batch.html"
    model = Batch
    context_object_name = "batch"
    slug_url_kwarg = "batchID"
    slug_field = "batch_id"

    def get_queryset(self, **kwargs):
        qs = (
            Batch.objects.select_related(
                "recipe",
                "volume_unit",
            )
            .prefetch_related(
                "step",
            )
            .filter(
                batch_id=self.kwargs.get("batchID"),
            )
            .order_by("createdAt")
        )
        return qs

    def get_context_data(self, **kwargs):
        # breakpoint()
        context_data = super().get_context_data(**kwargs)
        context_data.update({})
        return context_data
