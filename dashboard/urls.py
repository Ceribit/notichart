from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^remove_note/(?P<pk>\d+)/', views.remove_note, name = 'remove_note')
]
