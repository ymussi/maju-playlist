from maju.api import api
from maju.api.statistics import StatisticsManager
from flask_restplus import Resource
from flask import request

import logging

log = logging.getLogger(__name__)
ns = api.namespace('statistics', description="City statistics consulted.")


@ns.route('/')
class GetPartnerByCoordinates(Resource):
    def get(self):
        """
        Returns a statistic of the cities consulted.
        """
        statistcs = StatisticsManager().get_statistics()
        return statistcs