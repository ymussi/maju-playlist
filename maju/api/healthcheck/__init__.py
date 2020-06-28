from maju.database.models import LogCityTemp
from maju.database import session
import logging

def get_first_record():
    try:
        obj = session.query(LogCityTemp.id).first()
        session.close()
        if obj.id is not None:
            response = {
                    'message': 'The request was fulfilled.'}
            status_code = 200
        logging.info('Healthcheck: The request was fulfilled.')
        return response, status_code
    except Exception as e:
        response = {'message': 'The request had bad syntax or was inherently impossible to be satisfied.',
                    'err': str(e)}
        return response, 400