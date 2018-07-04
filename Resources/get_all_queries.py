from flask_restful import Resource
from flask_restful import reqparse
from Databases.config_database_C import ConfigDatabaseC
class GetAllQueries(Resource):
    def post(self):
        try: 
            # Parse the arguments
            mysql = ConfigDatabaseC.getMysql()
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('BuscaConsultas')
            data = cursor.fetchall()
            queries_list=[]
            for item in data:
                i = {
                    'id':item[0],
                    'cpf':item[1],
                    'date_time':item[2],
                    'result':item[3],
                }
                queries_list.append(i)

            return {'StatusCode':'200','Queries':queries_list}

        except Exception as e:
            return {'error': str(e)}