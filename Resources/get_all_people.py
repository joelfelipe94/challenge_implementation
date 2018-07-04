from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database_B import ConfigDatabaseB
from authnetication_manager_B import AuthenticationManagerB
class GetAllPeople(Resource):
    @AuthenticationManagerB.auth.login_required
    def post(self):
        try: 
            # Parse the arguments
            mysql = ConfigDatabaseB.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('BuscaPessoas')
            data = cursor.fetchall()
            debts_list=[];
            for item in data:
                i = {
                    'idade':item[0],
                    'endereco':item[1],
                    'fonte_de_renda':item[2],
                    'renda':item[3],
                }
                debts_list.append(i)

            return {'StatusCode':'200','Debts':debts_list}

        except Exception as e:
            return {'error': str(e)}