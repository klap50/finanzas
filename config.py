import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


# get environment variables
DB_HOST = config.get('localhost')
DB_PORT = config.get('3306')
DB_NAME = config.get('finanzas')
DB_USER = config.get('root')
DB_PASS = config.get('glider911')