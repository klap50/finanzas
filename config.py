import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# Get environment variables from config.ini
DB_HOST = config.get('database', 'DB_HOST')
DB_PORT = config.get('database', 'DB_PORT')
DB_NAME = config.get('database', 'DB_NAME')
DB_USER = config.get('database', 'DB_USER')
DB_PASS = config.get('database', 'DB_PASS')
