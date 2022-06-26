# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from supplies.models import Supply

django_logger = logging.getLogger("django")


# def indexView(request):
#     msg = "Welcome to the home of the Passata"
#     return render(request, "templates/index_template.html", {"msg": msg})


class SuppliesList(ListView):
    template_name = "supplies_list.html"
    model = Supply
    context_object_name = "supplies"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        msg = "Welcome to the home of the Passata"
        context_data.update({"msg": msg})
        return context_data


class SupplyView(DetailView):
    template_name = "supply.html"
    model = Supply
    context_object_name = "supply"
    # slug_url_kwarg = "supplID"
    # slug_field = "batch_id"

    # def get_queryset(self, **kwargs):
    #     qs = (
    #         Batch.objects.select_related(
    #             "recipe",
    #             "volume_unit",
    #         )
    #         .prefetch_related(
    #             "step",
    #         )
    #         .filter(
    #             batch_id=self.kwargs.get("batchID"),
    #         )
    #         .order_by("createdAt")
    #     )
    #     return qs

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update({})
        return context_data
