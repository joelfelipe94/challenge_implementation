from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database_A import ConfigDatabaseA
from authnetication_manager_A import AuthenticationManagerA

class CreateUserA(Resource):
    @AuthenticationManagerA.auth.login_required
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='Username to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()
            _username = args['username']
            _userPassword = args['password']
            mysql = ConfigDatabaseA.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('criaUsuario',(_username,_userPassword))
            data = cursor.fetchall()
            if len(data) is 0:
                conn.commit()
                return {'StatusCode':'200','Message': 'User creation success'}
            else:
                return {'StatusCode':'1000','Message': str(data[0])}
            return {'Username': args['username'], 'Password': args['password']}

        except Exception as e:
            return {'error': str(e)}
