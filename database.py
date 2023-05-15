import mysql.connector
import configparser
import os

# Read the configuration from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the database configuration values from the config.ini file or from environment variables
db_host = os.environ.get('DB_HOST', config['database']['host'])
db_port = os.environ.get('DB_PORT', config['database']['port'])
db_name = os.environ.get('DB_NAME', config['database']['database'])
db_user = os.environ.get('DB_USER', config['database']['user'])
db_password = os.environ.get('DB_PASSWORD', config['database']['password'])

def establecer_conexion():
    # Establish a connection to the database
    cnx = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return cnx
