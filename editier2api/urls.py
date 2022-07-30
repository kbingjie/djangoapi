"""editier2api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from editier2api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    # path("editier2/", views.EdiTier2.as_view(), name="testdata"), #FBVs
    path("datalist/", views.DataList.as_view(), name="DataList"),  # CBVs
    # path("editier2/", views.testdata),### FBVs with no authentication
    path("editier2/<int:id>", views.individual_data),
    # path("jobflow1/<int:id>", views.each_test),
    # for jobflow api
    path("jobflow/", views.JobFlowList.as_view(), name="JobFlowList"),
    path("jobflow/<int:pk>", views.EachJobFlow.as_view(), name="EachJobFlow"),
]
