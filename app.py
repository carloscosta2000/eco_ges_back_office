import copy
from getpass import getpass
import mysql.connector

cnx = mysql.connector.connect(user='seed', password='deesdees',
                              host='localhost',
                              database='remotedb')
cursor = cnx.cursor(prepared = True)

print("----------- Welcome to ECOGES back-office ----------\n" + 
"Please insert your login credentials:")
username = input("Username:")
password = getpass()
stmt = "SELECT nome, roleID FROM Employee WHERE username = %s and password = %s"
cursor.execute(stmt, (username,password))
queryResult = cursor.fetchone()
#print(type(queryResult[0]))
if (queryResult == None):
    print("Login failed! Username and/or password are incorrect. Please try again.")
    exit(1)
stmt = "SELECT tipo FROM Role WHERE id = %s"
cursor.execute(stmt, (queryResult[1],))
role = cursor.fetchone()[0]
print("Logged in!\nWelcome " + str(queryResult[0]) + ", with the " + role +" role.")