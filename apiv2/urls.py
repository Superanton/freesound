# -*- coding: utf-8 -*-

#
# Freesound is (c) MUSIC TECHNOLOGY GROUP, UNIVERSITAT POMPEU FABRA
#
# Freesound is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Freesound is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Authors:
#     See AUTHORS file.
#

# packages to install:
#   - django-oauth2-provider
#   - djangorestframework
#   - markdown (for browseable api)


from django.conf.urls.defaults import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from apiv2 import views
from provider.oauth2.views import Authorize, Redirect, Capture
from apiv2.utils import AccessTokenView

'''
urlpatterns = patterns('apiv2.views',
    url(r'^$', 'api_root'),
#    url(r'^sounds/$', views.SoundList.as_view(), name="sound-list"),
    url(r'^sounds/(?P<pk>[0-9]+)/$', views.SoundDetail.as_view(), name="apiv2-sound-detail"),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="apiv2-user-detail"),
    url(r'^users/(?P<pk>[0-9]+)/sounds/$', views.UserSoundList.as_view(), name="apiv2-user-sound-list"),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
'''

urlpatterns = patterns('apiv2.views',
       url(r'^apply/$', views.create_apiv2_key),
       url(r'^$', 'api_root'),
       #    url(r'^sounds/$', views.SoundList.as_view(), name="sound-list"),
       url(r'^sounds/(?P<pk>[0-9]+)/$', views.SoundDetail.as_view(), name="apiv2-sound-detail"),
       url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name="apiv2-user-detail"),
       url(r'^users/(?P<pk>[0-9]+)/sounds/$', views.UserSoundList.as_view(), name="apiv2-user-sound-list"),
       #url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
       url('^oauth2/authorize/?$', login_required(Capture.as_view()), name='oauth2:capture'),
       url('^oauth2/authorize/confirm/?$', login_required(Authorize.as_view()), name='oauth2:authorize'),
       url('^oauth2/redirect/?$', login_required(Redirect.as_view()), name='oauth2:redirect'),
       url('^oauth2/access_token/?$', csrf_exempt(AccessTokenView.as_view()), name='oauth2:access_token'),

       # Any other url
       url(r'/$', views.return_invalid_url ),
)

