from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from Resources.create_user_A import CreateUserA
from Resources.create_user_B import CreateUserB
from Resources.get_person import GetPerson
from Resources.get_all_people import GetAllPeople
from Databases.config_database_A import ConfigDatabaseA
from Databases.config_database_B import ConfigDatabaseB

from Resources.get_all_debts import GetAllDebts
from Resources.get_all_properties import GetAllProperties
import sys, inspect 

app = Flask(__name__)
api = Api(app)
ConfigDatabaseA(app) #it configures databaseA connection
ConfigDatabaseB(app) #it configures databaseB connection


# TODO make this associations automatically
#database A
api.add_resource(CreateUserA, '/CreateUserA')
api.add_resource(GetAllDebts, '/GetAllDebts')
api.add_resource(GetPerson, '/GetPerson')

#database B
api.add_resource(CreateUserB, '/CreateUserB')
api.add_resource(GetAllProperties, '/GetAllProperties')
api.add_resource(GetAllPeople, '/GetAllPeople')


if __name__ == '__main__':
    app.run(debug=True, port=5001, ssl_context=('certificate/cert.pem', 'certificate/key.pem'))

