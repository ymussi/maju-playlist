from maju.config import read_config
from werkzeug.exceptions import BadRequest, Unauthorized, UnprocessableEntity
import json, requests

class Weather:
    
    def __init__(self):
        self._cfg = read_config()
        self._url_weather = self._cfg.get("weather", 'url')
    
    def get_weather(self, city):
        try:
            request = requests.get(self._url_weather + city)            
            return request.json()
        except Exception as e:
            print(f"Error in function get_weather in class Weather - {str(e)}")
            
            return {'status': False, "err": f"Error in function get_weather in class Weather - {str(e)}"}
