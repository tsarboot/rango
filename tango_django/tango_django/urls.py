from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rango import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^rango/',include('rango.urls')),
    url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^login/',include('rango.urls')),
    url(r'^about/',include('rango.urls')),
    url(r'^categories/',include('rango.urls')),
    url(r'^media/',include('rango.urls')),
    path('admin/', admin.site.urls),
]
