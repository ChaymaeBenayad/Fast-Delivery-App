"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from landmark.views import (
    home_view,
    webpage1,
    webpage2,
    palce_proche,
    map_view,
    display_destination_reperes
    location_view,
    Contact_view,
    optimalPath_view,

)

from account.views import (
    registration_view,
    logout_view,
    login_view,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name="home"),
    path('myLocation/', location_view, name="MyLocation"),
    path('contactUs/',  Contact_view, name="ContactUs"),
    path('optimalPath/', optimalPath_view, name="optimalPath"),
    path('', login_view, name="login"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('test/',webpage1,name="webpage1"),
    path('optimal/',webpage2,name="webpage2"),
    path('trouver/', palce_proche, name="palce_proche"),
    path('mapTest/', map_view, name="map"),
    path('reperes/',display_destination_reperes,name="display_reperes"),
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
