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

from django.contrib import admin
from follow.models import FollowingUserItem, FollowingQueryItem

class FollowUserAdmin(admin.ModelAdmin):
    # raw_id_fields = ('last_post', )
    list_display = ('user_from', 'user_to', 'created')
    # list_filter = ('user_from', 'user_to', 'created')

admin.site.register(FollowingUserItem, FollowUserAdmin)

class FollowTagAdmin(admin.ModelAdmin):
    # raw_id_fields = ('user',)
    list_display = ('user', 'query')
    # list_filters = ('status',)
    # search_fields = ('=author__username', "title")

admin.site.register(FollowingQueryItem, FollowTagAdmin)