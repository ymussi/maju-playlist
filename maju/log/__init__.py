from maju.database.models import LogCityTemp
from maju.database import session
from datetime import datetime
import logging

class LoggerManager:
    
    def __init__(self, city_name, uf, temp, gender, provider,
                 weather_response, provider_response, status='success'):
        self.city_name = city_name
        self.uf = uf
        self.temp = temp
        self.music_gender = gender
        self.provider_response = provider_response
        self.weather_response = weather_response
        self.status = status
        self.provider = provider
    
    def save_log(self):
        try:
            log = LogCityTemp()
            log.city = self.city_name.title()
            log.uf = self.uf
            log.temp = self.temp
            log.music_gender = self.music_gender
            log.provider = self.provider
            log.status = self.status
            log.weather_response = self.weather_response
            log.provider_response = self.provider_response
            
            session.add(log)
            session.commit()
            
        except Exception as e:
            session.rollback()
            session.close()
            logging.error(f"Error when saving the query log. - {str(e)}")
