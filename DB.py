import psycogreen.eventlet
psycogreen.eventlet.patch_psycopg()  # Use it with eventlet workers 
from psycopg2 import connect
import json

class PosgresConnection:

    def __init__(self, config_filename):
        with open(config_filename, "r") as file:
            db_args = json.loads(file.read())
            pool_size = db_args.pop("pool_size")
        self.db_args = db_args

    def get_connection(self):
        """
        Function: get_connection
        Summary: Create a new connection from connection file
        Returns: psycopg2 connection
        """
        return connect(**self.db_args)  # Create a new cnnection

    def release_connection(self, connection):
        """
        Function: release_connection
        Summary: Close given connecrion
        Attributes: 
            @param (connection): Postgrest connection
        Returns: Status boolean
        """
        try:
            connection.close()
            return True
        except Exception as e:
            logging.debug(str(e))  # Caching erorrs and reporting
            return False