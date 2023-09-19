import traceback
from databases.DatabaseConnector import DatabaseConnector

class DatabaseWrapper:
    def call(self, stored_procedure_name, parameters):
        try:
            databaseConnector =  DatabaseConnector('TuRoot','TuPassword','localhost','3306','TuBaseDeDatos')
            databaseConnector.open_mysql_connection()
            databaseConnector.call_stored_procedure ( stored_procedure_name, parameters)


        except Exception as err:
            error_message= traceback.format_exc()
            print(error_message)
            raise err


        finally:
            if databaseConnector:
                databaseConnector.close_mysql_connection()
