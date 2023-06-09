import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect('cancer.db')
        self.cursor = self.con.cursor()
        self.create_users_table()
        self.create_diagnoses_table()

    '''CREATE the Login TABLE'''
    def create_users_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, fullname varcahr(50) NOT NULL, email varchar(50) NOT NULL, password varchar(50) NOT NULL, dob varchar(20) NOT NULL, phone_no varchar(20) NOT NULL)")
    
    '''CREATE the diagnoses TABLE'''
    def create_diagnoses_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS diagnoses(id integer PRIMARY KEY AUTOINCREMENT, symptoms text NOT NULL, result varchar(100) NOT NULL, comment varchar(50) NOT NULL, diagnose_date varchar(20), user_id integer NOT NULL)")

    '''Register User'''
    def register_user(self, fullname, email, password, phone_no, dob):
        self.cursor.execute("INSERT INTO users(fullname, email, password, dob, phone_no) VALUES(?, ?, ?, ?, ?)", (fullname, email, password, dob, phone_no))
        self.con.commit()

        # Getting the last user
        user = self.cursor.execute("SELECT * FROM users ").fetchall()
        return user[-1]
    
    '''Getting Login User by Username'''
    def get_user(self, email):
        # Get the user by username
        user = self.cursor.execute("SELECT * FROM users where email =?", (email,)).fetchone()
        return user
    
    '''Save diagnose'''
    def save_diagnose(self, symptoms, result, comment, diagnose_date, user_id):
        
        # Saving diagnose result
        self.cursor.execute("INSERT INTO diagnoses(symptoms, result, comment, diagnose_date, user_id) VALUES(?, ?, ?, ?, ?)", 
                            (
            symptoms, result, comment, diagnose_date, user_id
            ))
        self.con.commit()


    '''View diagnoses by a user'''
    def view_diagnose(self, userid):
        diagnose = self.cursor.execute("SELECT * FROM diagnoses WHERE user_id=?",(userid,)).fetchall()
        return diagnose
        

    # def mark_task_as_incomplete(self, taskid):
    #     self.cursor.execute("UPDATE tasks SET completed=0 WHERE id=?",(taskid,))
    #     self.con.commit()
        
    #     # returning the task text
    #     task_text = self.cursor.execute("SELECT task FROM tasks WHERE id=?", (taskid,)).fetchall()
    #     return task_text[0][0]

    '''Deleting the diagnose'''
    def delete_diagnose(self, id):
        self.cursor.execute("DELETE FROM diagnoses WHERE id=?", (id,))
        self.con.commit()

    '''Closing the connection '''
    def close_db_connection(self):
        self.con.close()