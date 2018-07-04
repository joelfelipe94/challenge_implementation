from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database import ConfigDatabase
class AuthenticateUser(Resource):
    def post(self):
        try:
            # Parse the arguments

            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, help='Email address for Authentication')
            parser.add_argument('password', type=str, help='Password for Authentication')
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']
            mysql = ConfigDatabase.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_AuthenticateUser',(_userEmail,))
            data = cursor.fetchall()
            if(len(data)>0):
                if(str(data[0][2])==_userPassword):
                    return {'status':200, 'UserId':str(data[0][0])}
                else:
                    return {'status':100, 'message':'Authentication failure'}
            else:
                return {'status':1000, 'message':'This user doesnt exist'}
        except Exception as e:
            return {'error': str(e)}