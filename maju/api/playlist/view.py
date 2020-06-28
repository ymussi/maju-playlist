from maju.api import api
from maju.api.playlist.controller import PlaylistManager
from flask_restplus import Resource
from flask import request

import logging

log = logging.getLogger(__name__)
ns = api.namespace('playlist', description="Find a playlist according to the city's temperature.")


@ns.route('/<string:city>')
class GetPartnerByID(Resource):
    def get(self, city):
        """
        Find a playlist according to the city's temperature.
        """
        playlist = PlaylistManager().get_playlist_by_city_temper(city)
        return playlist
