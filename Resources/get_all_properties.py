from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database_B import ConfigDatabaseB
from authnetication_manager_B import AuthenticationManagerB
class GetAllProperties(Resource):
    @AuthenticationManagerB.auth.login_required
    def post(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('id_pessoa', type=str)
            args = parser.parse_args()

            _id_pessoa = args['id_pessoa']

            mysql = ConfigDatabaseB.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('BuscaBens',(_id_pessoa,))
            data = cursor.fetchall()
            preperties_list=[]
            for item in data:
                i = {
                    'id_bem':item[0],
                    'valor':item[1],    
                    'descricao':item[2],
                }
                preperties_list.append(i)

            return {'StatusCode':'200','Properties':preperties_list}

        except Exception as e:
            return {'error': str(e)}