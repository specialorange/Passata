from django.urls import re_path

from . import views

app_name = "batch"

urlpatterns = [
    re_path(r"all/?", views.BatchesView.as_view(), name="all"),
    re_path(
        r"^(?P<batchID>[a-zA-Z0-9-\w:]+)/?",
        views.BatchView.as_view(),
        name="single",
    ),
]

# account_urls = [
# urlpatterns = [
#     path("mechanic/", include((mechanic_urls, "jobs"), namespace="mechanic")),
#     path("account/", include((account_urls, "jobs"), namespace="account")),
