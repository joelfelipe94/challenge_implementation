from flask_restful import Resource
from flask_restful import reqparse
from flask_httpauth import HTTPBasicAuth
from Databases.config_database import ConfigDatabase
class AuthenticationManager:
    auth = HTTPBasicAuth()
    @auth.verify_password
    def verify_password(username, password):
        # Parse the arguments
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help='Email address for Authentication')
        parser.add_argument('password', type=str, help='Password for Authentication')
        args = parser.parse_args()
        _userEmail = username
        _userPassword = password
        mysql = ConfigDatabase.getMysql()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_AuthenticateUser',(_userEmail,))
        data = cursor.fetchall()
        if(len(data)>0):
            if(str(data[0][2])==_userPassword):
                return True
            else:
                return False
        else:
            return False