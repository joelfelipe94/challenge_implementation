from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database import ConfigDatabase
from authnetication_manager import AuthenticationManager
class AddItem(Resource):
    @AuthenticationManager.auth.login_required
    def post(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('item', type=str)
            args = parser.parse_args()

            _userId = args['id']
            _item = args['item']

            mysql = ConfigDatabase.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_AddItems',(_userId,_item))
            data = cursor.fetchall()
            conn.commit()
            return {'StatusCode':'200','Message': 'Success'}

        except Exception as e:
            return {'error': str(e)}