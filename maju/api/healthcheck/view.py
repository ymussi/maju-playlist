from maju.api import api
from maju.api.healthcheck import get_first_record
from flask_restplus import Resource

import logging

log = logging.getLogger(__name__)
ns = api.namespace('healthcheck', description='Communication test.')

@ns.route('/')
class HealhCheck(Resource):
    @ns.response(code=400, description='Bad Request')
    def get(self):
        """
        Healhcheck endpoint.
        """
        return get_first_record()
