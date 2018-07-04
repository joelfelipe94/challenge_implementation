from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database_A import ConfigDatabaseA
from authnetication_manager_A import AuthenticationManagerA
class GetPerson(Resource):
    @AuthenticationManagerA.auth.login_required
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
            cursor.callproc('BuscaPessoa',(_cpf,))
            data = cursor.fetchall()
            print(data)
            debts_list=[];
            for item in data:
                i = {
                    'nome':item[0],
                    'endereco':item[1],
                }
                debts_list.append(i)

            return {'StatusCode':'200','Debts':debts_list}

        except Exception as e:
            return {'error': str(e)}