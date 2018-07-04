from flask import Flask
from flask_restful import Api
from flaskext.mysql import MySQL
class ConfigDatabase:
    _mysql = None
    @staticmethod
    def getMysql():
        return ConfigDatabase._mysql 
    def __init__(self, app):
        """ Virtually private constructor. """
        if ConfigDatabase._mysql != None:
            raise Exception("This class is already configured!")
        else:
            ConfigDatabase._mysql = MySQL()
            # MySQL configurations
            app.config['MYSQL_DATABASE_USER'] = 'joel'
            app.config['MYSQL_DATABASE_PASSWORD'] = 'akhenatom94'
            app.config['MYSQL_DATABASE_DB'] = 'ItemListDb'
            app.config['MYSQL_DATABASE_HOST'] = 'localhost'
            ConfigDatabase._mysql.init_app(app)
