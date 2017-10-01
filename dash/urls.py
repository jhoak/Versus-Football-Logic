from django.conf.urls import url
from django.conf.urls.static import static
from django.http import Http404
from django.conf import settings

from . import views

def _raise404(request):
	raise Http404("Couldn't find the page you requested.")

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dash/loginview', views.showlogin, name='showlogin'),
    url(r'^dash/login$', views.login, name='login'),
    url(r'^dash/signout$', views.signout, name='signout'),
    url(r'^dash/makeateam', views.makeateam, name='makeateam'),
    url(r'^dash/createteam$', views.createteam, name='createteam'),
    url(r'^dash', views.dashboard, name='dashboard'),
    url(r'^teams/(?P<team_name>[A-Za-z_]+)', views.showteam, name='showteam'),
    url(r'^teams', views.allteams, name='allteams'),
    url(r'^schedule', views.show_schedule, name='show_schedule'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
