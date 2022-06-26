"""passata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from passata import views as passataViews
from project.views import views as projectViews
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import include
urlpatterns = [
    re_path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    re_path(r"adminpanel/?", admin.site.urls),
    re_path("__debug__/", include("debug_toolbar.urls")),
    # include(("jobs.urls", "jobs"), namespace="jobs")),
    re_path(r"^batches/", include("batch.urls", namespace="batches")),
    re_path(r"^supplies/", include("supplies.urls", namespace="supplies")),
    re_path("", projectViews.indexView.as_view(), name="indexView"),
]
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
