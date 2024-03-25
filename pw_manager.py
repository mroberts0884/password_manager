import secrets
import sqlite3
import random
import string

try:
        conn = sqlite3.connect('credentials.db')
except:
        print("error")
#cursor object
cursor_obj = conn.cursor()

#def create_table():
#Create Table
    #credentials = ('CREATE TABLE IF NOT EXISTS Credentials (Username, Password)')
    #cursor_obj.execute(credentials)
    #print("table created")

#create_table()

#Enter Username and Password
def data_entry():
    username = input("Create Username: ")
    pw_length = input("Enter Password Length: ")
    characters = string.ascii_letters + string.digits + "!@#$%&*()"
    password = ''.join(secrets.choice(characters) for i in range(int(pw_length)))
    salt = random.randint(1000,9999)
    newPassword = f"{password}{str(salt)}"
    newPassword = hash(newPassword)
    cursor_obj.execute("INSERT INTO Credentials (Username, Password) VALUES (?, ?)", 
                       (username, newPassword))
    conn.commit()

data_entry()
cursor_obj.close()
conn.close()




