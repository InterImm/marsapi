from flask_restplus import fields
from marsapi.api.restplus import api

timekeeping_mars_interimm = api.model('Timekeeping on Mars Standard', {
    'year': fields.Integer(readOnly=True, description='Year on Mars'),
    'month': fields.Integer(readOnly=True, description='Month on Mars'),
    'day': fields.Integer(readOnly=True, description='Day on Mars'),
    'hour': fields.Integer(readOnly=True, description='Hour on Mars'),
    'minute': fields.Integer(readOnly=True, description='minute on Mars')
    })

timekeeping_mars_standard = api.model('Timekeeping on Mars Standard', {
    'day': fields.Integer(readOnly=True, description='Day on Mars'),
    'hour': fields.Integer(readOnly=True, description='Hour on Mars'),
    'minute': fields.Integer(readOnly=True, description='minute on Mars'),
    'second': fields.Integer(readOnly=True, description='second on Mars'),
    'millisecond': fields.Integer(readOnly=True, description='millisecond on Mars')
    })

timekeeping_mars_time = api.model('Timekeeping on Mars', {
    'martian_standard': fields.Nested(timekeeping_mars_standard),
    'mars_timezone': fields.Integer(readOnly=True, description='timezone on Mars'),
    'earth_utc_time': fields.String(readOnly=True, description='Current UTC time on Earth'),
})