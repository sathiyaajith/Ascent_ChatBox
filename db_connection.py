import sqlite3
##import config as c
from sqlite3 import Error
 
class SQLiteConnector():
    """SQLLite Database functionalities are defined in this class.
    
    """
    def __init__(self):
        """Constructor for class SQLite DB to connect to database.
        
        """
        self.db_file = db
        #self.connect()
        
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)
        
        return self.conn
        
    
    def query_exec(self, query):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        con = self.connect()
        with con:
            cur = con.cursor()
            cur.execute(query)     
            rows = cur.fetchall()
            #print(rows)
        cur.close()     
              
        return rows
    
    def close(self):
        """Closes the cursor and connection of the database.
        
        """
        
        
        self.conn.close()
        
 
