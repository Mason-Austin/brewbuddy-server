"""brewbuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from brewbuddyapi.views import register_user, check_user, BrewView, BrewLogView, CategoryView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'brews', BrewView, 'brew')
router.register(r'brew_logs', BrewLogView, 'brew_log')
router.register(r'categories', CategoryView, 'category' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('checkuser', check_user),
    path('', include(router.urls))
]
