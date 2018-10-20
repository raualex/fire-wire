import sqlite3


#database class handles connection to database, loading to databse and closes the connection to database
class Load_database:
   #initlaise the database connection and create table if not exists
   def __init__(self):
     print("Connecting to database")

     dbpath = "users.db"
     #connect to database
     self.conn = sqlite3.connect(dbpath, detect_types=sqlite3.PARSE_DECLTYPES)
     #enable FOREIGN KEY constrain
     self.conn.execute("PRAGMA foreign_keys = ON")

     #create USER table
     self.conn.execute('''CREATE TABLE IF NOT EXISTS USER (USER_ID INTEGER  PRIMARY KEY AUTOINCREMENT,
                                                   
                                                  USERNAME  TEXT NOT NULL,
                                                  PASSWORD  TEXT NOT NULL, 
                                                  FIRST_NAME TEXT NOT NULL ,             
                                                  LAST_NAME TEXT,
                                                  ADDRESS   TEXT NOT NULL
                                                      )''')

     self.conn.commit()
   
   #close database connection      
   def close(self):
     print("Closing the connection to database ...")
     self.conn.close()


   #    load the database(TRADEMARK_MODEL table) from trademark dictonary
   def load_database(self,user_obj): 
     print("Loading the data ...")

     #load data from the trademark dictonary
     cursor =  self.conn.cursor()
     #user_obj contains -> 
     cursor.execute("INSERT INTO USER (USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,ADDRESS,DESTINATION,PHONE,EMAIL) VALUES (?, ?, ?,?, ?,?,?,?)",( str(user_obj.username), str(user_obj.password), str(user_obj.first_name),str(user_obj.last_name),str(user_obj.address),str(user_obj.destination), user_obj.phone, str(user_obj.email) ))
       
     self.conn.commit()

   def check_user(self,username):
       cursor =  self.conn.cursor()
       exists = False    
       try:
          cursor.execute("SELECT USER_ID from USER where USERNAME = ?", (username,))
          exists = bool(cursor.fetchone())

       except sqlite3.OperationalError as e:
          message = e.args[0]
  
       return exists


