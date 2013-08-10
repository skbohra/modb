from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
from movie.models import Movie

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from movie.views import *
from person.views import *
from lists.views import *

class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

#
# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
#router.register(r'movie', MovieViewSet)

admin.autodiscover()


urlpatterns = patterns("",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    #url(r"^", include("gatekeeper.urls")),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^', include(router.urls)),
    url(r'^movie/$', MovieList.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/$', MovieDetail.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/cast/$', CastList.as_view()),
    url(r'^movie/(?P<id>[0-9]+)/cast/(?P<pk>[0-9])/$', CastDetail.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/crew/$', CrewList.as_view()),
    url(r'^movie/(?P<id>[0-9]+)/crew/(?P<pk>[0-9])/$', CrewDetail.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/revenue/$', RevenueList.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/releases/$',ReleaseList.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/images/$',ImageList.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/images/(?P<type>[a-z]+)/$',ImageTypesList.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/videos/$',VideoList.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/videos/(?P<type>[a-z]+)/$',VideoTypesList.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/productions/$',ProductionCompanies.as_view()),
    url(r'^movie/(?P<pk>[0-9]+)/lists/$',MovieRelatedLists.as_view()),

    url(r'^person/$', PersonList.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/$', PersonDetail.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/images/$',PersonImageList.as_view()),
    url(r'^person/(?P<pk>[0-9]+)/lists/$',PersonRelatedLists.as_view()),
    url(r'^lists/$',MListsView.as_view()),
    url(r'^lists/(?P<pk>[0-9]+)/$',MListsDetail.as_view()),
    url(r'^lists/(?P<pk>[0-9]+)/add_movie/$',MListAdd.as_view()),

    url(r'^api-docs/', include('rest_framework_swagger.urls')),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
