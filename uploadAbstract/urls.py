from django.conf.urls import url, patterns
from uploadAbstract import views


urlpatterns = [url(r'^$', views.index, name='uploadAbstract'),]
