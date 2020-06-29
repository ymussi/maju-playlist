from maju.log import LoggerManager
from maju.utils.deezer import DeezerSearch
from maju.utils.spotify import SpotifySearch
from maju.utils.weather import Weather
from maju.config import read_config
from werkzeug.exceptions import BadRequest, Unauthorized, UnprocessableEntity

class PlaylistServices:
    
    def __init__(self, city_name):
        self._city_name = city_name.lower()
        self._provider = None
        self._city_temper = None
        self._provider_response = None
        self._weather_response = None
        self._uf = None
        
    def get_city_temper(self):
        try:
            weather_response = Weather().get_weather(self._city_name)
            if weather_response.get('by') == "city_name":
                self._city_temper = weather_response.get('results').get('temp')
                self._uf = weather_response.get('results').get('city').split(',')[1].strip()
                self._weather_response = weather_response
                response = {'status': True, 'temp': self._city_temper}
            else:
                response =  {'status': False, 'message': 'City not found.'}
                self._weather_response = response
                
            return response
        except Exception as e:
            print(
                f"Error in function get_city_temper in class PlaylistServices - msg: '{self._weather_response.get('message')}' - err: {str(e)}")
            self._weather_response = Weather().get_weather(self._city_name)
            return {'status': False, 'temp': self._weather_response.get('message'), 'err': str(e)}
    
    def parser_temp_to_gender(self):
        get_temper = self.get_city_temper()
        temp = get_temper.get('temp')
        gender = None
        if get_temper.get('status'):
            gender = 'classic'
            if temp >= 10 and temp <= 25:
                gender = 'rock'
            elif temp > 25:
                gender = 'pop'
            
        return gender
        
    def get_playlist(self):
        gender = self.parser_temp_to_gender()
        errors = []
        playlist = []
        count = 0
        try:
            while playlist == []:
                count += 1
                musics = SpotifySearch().get_playlist(gender)
                if musics.get('status'):
                    self._provider_response = musics
                    self._provider = 'Spotify'
                    playlist = musics.get('playlist')
                    break
                else:
                    errors.append({'Spotify': {'attempt': count, 'err': musics.get('err')}})
                    self._provider_response = errors
                
                musics = DeezerSearch().get_playlist(gender)
                if musics.get('status'):
                    self._provider_response = musics
                    self._provider = 'Deezer'
                    playlist = musics.get('playlist')
                    break
                else:
                    errors.append({'Deezer': {'attempt': count, 'err': musics.get('err')}})
                    self._provider_response = errors
                                
                if count == 5:
                    break
                
            if playlist == []:
                LoggerManager(city_name=self._city_name, uf=self._uf, temp=self._city_temper, gender=gender, provider=self._provider,
                          provider_response=self._provider_response, weather_response=self._weather_response, status='filed').save_log()
                return "Oh no.. ): Something went wrong, please try again later."
            
            LoggerManager(city_name=self._city_name, uf=self._uf, temp=self._city_temper, gender=gender, provider=self._provider,
                          provider_response=self._provider_response, weather_response=self._weather_response).save_log()
                
            return playlist
        except Exception as e:
            print(f"Error in function get_playlist in class PlaylistServices - {str(e)}")
            
            LoggerManager(city_name=self._city_name, uf=self._uf, temp=self._city_temper, gender=gender, provider=self._provider,
                          provider_response=self._provider_response, weather_response=self._weather_response, status='filed').save_log()
            
            return {'status': False, 'err': str(e)}
