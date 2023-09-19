import mysql.connector

class DatabaseConnector:

    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.use_unicode = True
    
    def open_mysql_connection(self):
        conn = mysql.connector.connect(user=self.user, password=self.password, host=self.host, port=self.port, database=self.database, use_unicode=self.use_unicode)
        self.conn=conn
    
    def close_mysql_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
    
    # call the mysql stored procedure. 
    def call_stored_procedure(self, stored_procedure_name, parameters):
        try:
            cursor = self.conn.cursor()
            out_args = cursor.callproc(stored_procedure_name, parameters)
            results = [r.fetchall() for r in cursor.stored_results()]
            self.conn.commit()
            cursor.close()
        except Exception as err:
            self.conn.rollback()
            raise err
            
        finally:
            pass

        return results
