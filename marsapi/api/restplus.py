import logging
import traceback

from flask_restplus import Api
from marsapi import settings

MARSAPI_CONFIG = {
        "version": "0.0.1",
        "title": "MarsAPI",
        "description": "Get Mars related information through API"
        }

log = logging.getLogger(__name__)

api = Api(**MARSAPI_CONFIG)


@api.errorhandler
def default_error_handler(e):
    message = 'Something is not right, Scott.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
