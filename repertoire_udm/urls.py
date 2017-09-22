from django.conf.urls import url, include
from django.contrib import admin

from .views import home_view, logout_view
from repertoire import views

urlpatterns = [
        url(r'^$', views.ElementList.as_view(), name='home'),
        url(r'^logout$', logout_view, name='logout'),
        url(r'^admin/', admin.site.urls),
        url(r'^search/', include('haystack.urls')),
        url(r'^', include('repertoire.urls')),
]
