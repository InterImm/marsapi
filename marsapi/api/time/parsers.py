from flask_restplus import reqparse

timekeeping_arguments = reqparse.RequestParser()
timekeeping_arguments.add_argument('earth_utc_time', type=float, required=False, default=1, help='UTC time on Mars')
timekeeping_arguments.add_argument(
    'mars_timezone', type=int, 
    required=False, 
    choices=[
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
        21, 22, 23, 24
    ],
    default=0, help='Timezone on Mars')
