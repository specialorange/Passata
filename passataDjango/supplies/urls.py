from django.urls import re_path

from . import views

app_name = "supplies"

urlpatterns = [
    re_path(r"all/?", views.SuppliesList.as_view(), name="all"),
    re_path(
        r"^(?P<pk>[a-zA-Z0-9-\w:]+)/?",
        views.SupplyView.as_view(),
        name="single",
    ),
]

# account_urls = [
# urlpatterns = [
#     path("mechanic/", include((mechanic_urls, "jobs"), namespace="mechanic")),
#     path("account/", include((account_urls, "jobs"), namespace="account")),
