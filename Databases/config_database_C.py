from flask import Flask
from flask_restful import Api
from flaskext.mysql import MySQL
class ConfigDatabaseC:
    _mysql = None
    @staticmethod
    def getMysql():
        return ConfigDatabaseC._mysql 
    def __init__(self, app):
        """ Virtually private constructor. """
        if ConfigDatabaseC._mysql != None:
            raise Exception("This class is already configured!")
        else:
            ConfigDatabaseC._mysql = MySQL()
            # MySQL configurations
            app.config['MYSQL_DATABASE_USER'] = 'userC'
            app.config['MYSQL_DATABASE_PASSWORD'] = 'userC'
            app.config['MYSQL_DATABASE_DB'] = 'base_C'
            app.config['MYSQL_DATABASE_HOST'] = 'localhost'
            ConfigDatabaseC._mysql.init_app(app)
