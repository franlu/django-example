from django.conf.urls import url

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
]
