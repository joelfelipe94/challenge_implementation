from flask_restful import Resource
from flask_restful import reqparse
from flask_httpauth import HTTPBasicAuth
from Databases.config_database_B import ConfigDatabaseB
class AuthenticationManagerB:
    auth = HTTPBasicAuth()
    @auth.verify_password
    def verify_password(username, password):
        # Parse the arguments
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='Username for Authentication')
        parser.add_argument('password', type=str, help='Password for Authentication')
        args = parser.parse_args()
        _username = username
        _userPassword = password
        mysql = ConfigDatabaseB.getMysql()
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('AutenticaUsusario',(_username,))
        data = cursor.fetchall()
        print(data)
        if(len(data)>0):
            if(str(data[0][1])==_userPassword):
                return True
            else:
                return False
        else:
            return False