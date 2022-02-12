"""expenses URL Configuration

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
from django.db import router
from django.urls import path
from django.urls import include
from car.views import CarPlanViewset, CarSpecificationViewset
from users.views import RegsiterView, VerifyEmail 
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from rest_framework.routers import DefaultRouter

schema_view = get_schema_view(
    openapi.Info(
        title="Coding API",
        default_version = 'v1',
        description = "Test description",
        terms_of_serivice ='htpps://www.google.com/policies/terms/',
        contact = openapi.Contact(email="contact@sanippets.local"),
        license= openapi.License(name="BSD License"),

    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
)

router = DefaultRouter()
router.register('carspecs/', CarSpecificationViewset, basename='car'),
router.register('carplan/',CarPlanViewset, basename='carplan')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include(router.urls)),
    path('register/', RegsiterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui')
]
