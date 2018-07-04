from flask import Flask
from flask_restful import Api
from flaskext.mysql import MySQL
class ConfigDatabaseA:
    _mysql = None
    @staticmethod
    def getMysql():
        return ConfigDatabaseA._mysql 
    def __init__(self, app):
        """ Virtually private constructor. """
        if ConfigDatabaseA._mysql != None:
            raise Exception("This class is already configured!")
        else:
            ConfigDatabaseA._mysql = MySQL()
            # MySQL configurations
            app.config['MYSQL_DATABASE_USER'] = 'userA'
            app.config['MYSQL_DATABASE_PASSWORD'] = 'userA'
            app.config['MYSQL_DATABASE_DB'] = 'base_A'
            app.config['MYSQL_DATABASE_HOST'] = 'localhost'
            ConfigDatabaseA._mysql.init_app(app)
