"""beer_warehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView
from rest_framework import routers

from beers.api import views
from beers.api.views import UserListAPI
from beers.views import LoginPrueba

"""router = routers.DefaultRouter()
router.register('beers',views.BeerViewSet)
router.register('company',views.CompanyViewSet)
router.register('users',views.UserViewSet)
router.register('recetas',views.RecetaViewSet)"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beers/', include('beers.urls')),
    path('accounts/',include('django.contrib.auth.urls'), name='sign-in'),
    #url('',RedirectView.as_view(url='/beers/list/')),
    url('pruebalogin/',LoginPrueba.as_view(),name='loginPrueba'),
    #url('api/',include(router.urls)),

    # User API URLs
    url(r'^api/1.0/usuarios/$', UserListAPI.as_view(),name='user-list-api')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
