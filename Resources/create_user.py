from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database import ConfigDatabase
from authnetication_manager import AuthenticationManager

class CreateUser(Resource):
    #@ApiConfig.app.route('/CreateUser')
    @AuthenticationManager.auth.login_required
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()
            _userEmail = args['email']
            _userPassword = args['password']
            mysql = ConfigDatabase.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('spCreateUser',(_userEmail,_userPassword))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200','Message': 'User creation success'}
            else:
                return {'StatusCode':'1000','Message': str(data[0])}
            return {'Email': args['email'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}
