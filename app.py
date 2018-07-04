from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from Resources.get_all_items import GetAllItems
from Resources.add_item import AddItem
from Resources.create_user import CreateUser
from Resources.create_user_A import CreateUserA
from Resources.get_person import GetPerson
from Databases.config_database import ConfigDatabase
from Databases.config_database_A import ConfigDatabaseA
from Resources.get_all_debts import GetAllDebts
import sys, inspect 

app = Flask(__name__)
api = Api(app)
ConfigDatabase(app) #it configures a database connection
ConfigDatabaseA(app) #it configures a databaseA connection

# TODO make this associations automatically
#database A
api.add_resource(CreateUserA, '/CreateUserA')
api.add_resource(GetAllDebts, '/GetAllDebts')
api.add_resource(GetPerson, '/GetPerson')

#basic idea
api.add_resource(CreateUser, '/CreateUser')
api.add_resource(GetAllItems, '/GetAllItems')
api.add_resource(AddItem, '/AddItem')

if __name__ == '__main__':
    app.run(debug=True, port=5001, ssl_context=('certificate/cert.pem', 'certificate/key.pem'))

