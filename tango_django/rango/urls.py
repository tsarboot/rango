from django.conf.urls import url
from rango import views
from django.conf import settings
from django.urls import path 
from django.conf.urls.static import static

app_name = 'rango'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^categories/(?P<category_name_slug>[\w\-]+)/$',views.show_category,name='categories'),
    url(r'^add_cat/',views.add_category,name='add_cat'),
    path('<str:car_name>',views.carName,name='cars'),
    url(r'^search/',views.search,name='search'),
    url(r'^about/',views.about,name='about')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
