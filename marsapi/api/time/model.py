from flask_restplus import fields
from marsapi.api.restplus import api

timekeeping_mars_time = api.model('Timekeeping on Mars', {
    'year': fields.Integer(readOnly=True, description='Year on Mars'),
    'month': fields.Integer(readOnly=True, description='Month on Mars'),
    'day': fields.Integer(readOnly=True, description='Day on Mars'),
    'hour': fields.Integer(readOnly=True, description='Hour on Mars'),
    'minute': fields.Integer(readOnly=True, description='minute on Mars'),
    'mars_timezone': fields.Integer(readOnly=True, description='timezone on Mars'),
    'earth_utc_time': fields.String(readOnly=True, description='Current UTC time on Earth'),
})