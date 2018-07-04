from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database_A import ConfigDatabaseA
class GetAllDebts(Resource):
    def post(self):
        try: 
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('cpf', type=str)
            args = parser.parse_args()

            _cpf = args['cpf']

            mysql = ConfigDatabaseA.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('BuscaDividas',(_cpf,))
            data = cursor.fetchall()
            print(data)
            debts_list=[];
            for item in data:
                i = {
                    'id_divida':item[0],
                    'valor':item[1],    
                    'credor':item[2],
                }
                debts_list.append(i)

            return {'StatusCode':'200','Debts':debts_list}

        except Exception as e:
            return {'error': str(e)}