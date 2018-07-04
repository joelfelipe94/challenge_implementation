from flask import Flask
from flask_restful import Api
from flaskext.mysql import MySQL
class ConfigDatabaseB:
    _mysql = None
    @staticmethod
    def getMysql():
        return ConfigDatabaseB._mysql 
    def __init__(self, app):
        """ Virtually private constructor. """
        if ConfigDatabaseB._mysql != None:
            raise Exception("This class is already configured!")
        else:
            ConfigDatabaseB._mysql = MySQL()
            # MySQL configurations
            app.config['MYSQL_DATABASE_USER'] = 'userB'
            app.config['MYSQL_DATABASE_PASSWORD'] = 'userB'
            app.config['MYSQL_DATABASE_DB'] = 'base_B'
            app.config['MYSQL_DATABASE_HOST'] = 'localhost'
            ConfigDatabaseB._mysql.init_app(app)
