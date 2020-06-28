from maju.api.playlist.service import PlaylistServices
from werkzeug.exceptions import BadRequest
import re

class CityValidations:
    
    def city_name(self, city):
        temp = PlaylistServices(city).get_city_temper()
        
        if city.isdigit():
            raise BadRequest("'city' must contain a string of characters ('Campinas'), not numerical ('123456').")
        
        if not temp.get('status'):
            raise BadRequest(temp.get('temp'))
                       