from maju.database import session
from maju.database.models import LogCityTemp
from werkzeug.exceptions import BadRequest
import logging, json

class StatisticsManager:
    
    def get_statistics(self):
        try:
            statistics = []
            query = LogCityTemp.get_statistics()
            for obj in query:
                city = {
                    'city': obj.city,
                    'uf': obj.uf,
                    'count': obj.count,
                    'last_created': str(obj.last_created)
                }
                statistics.append(city)

            return statistics
        except Exception as e:
            print(f"Error in function get_statistics in class StatisticsManager - {str(e)}")
            
            return {'status': False, 'err': str(e)}
