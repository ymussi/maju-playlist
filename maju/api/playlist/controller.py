from maju.api.playlist.service import PlaylistServices
from maju.utils.validations import CityValidations
from werkzeug.exceptions import BadRequest
import logging

class PlaylistManager:
    
    def get_playlist_by_city_temper(self, city):
        city_valid = CityValidations().city_name(city)
        return PlaylistServices(city).get_playlist()
