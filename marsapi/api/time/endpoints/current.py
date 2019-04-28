import logging

import datetime

from flask import request
from flask_restplus import Resource
from marsapi.api.time.business import earth_utc_to_mars_aat
from marsapi.api.time.model import timekeeping_mars_time
from marsapi.api.time.parsers import timekeeping_arguments
from marsapi.api.restplus import api

log = logging.getLogger(__name__)

ns = api.namespace('time/current', description='Get current time on Mars')

@ns.route('/')
class GetDateTimeNow(Resource):

    @api.expect(timekeeping_arguments)
    @api.marshal_with(timekeeping_mars_time)
    def get(self):
        """
        Get time on Mars
        """
        dt_now = datetime.datetime.utcnow().isoformat()
        args = timekeeping_arguments.parse_args(request)
        earth_utc_time = args.get('earth_utc_time', dt_now)
        mars_timezone = args.get('mars_timezone', 0)

        mars_aat_time = earth_utc_to_mars_aat(earth_utc_time)

        res = {
            "earth_utc_time": dt_now,
            "mars_timezone": mars_timezone
        }

        return res
