from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database_C import ConfigDatabaseC
class GetMovements(Resource):
    def post(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('cpf', type=str)
            args = parser.parse_args()

            _cpf = args['cpf']

            mysql = ConfigDatabaseC.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('BuscaMovimentosCPF',(_cpf,))
            data = cursor.fetchall()
            movements_list=[];
            for item in data:
                i = {
                    'id_movement':item[0],
                    'value':item[1],    
                    'description':item[2],
                }
                movements_list.append(i)

            return {'StatusCode':'200','Movement':movements_list}

        except Exception as e:
            return {'error': str(e)}