import copy
from getpass import getpass
import sys
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
if (role == "Marketing"):
    while (True):
        print("Operations: (S)ee all customers; (C)reate new add; (E)xit")
        op = input()
        if (op == "S" or op == "s"):
            print("Clientes:")
            stmt = "SELECT nome, username FROM Client"
            cursor.execute(stmt)
            queryResult = cursor.fetchall()
            for customer in queryResult:
                print("Nome: " + customer[0] + " Username: " + customer[1])
        elif (op == "C" or op == "c"):
            #statement
            print()
        elif (op == "E" or op == "e"):
            sys.exit();
elif (role == "Account Manager"):
    while (True):
        print("Operations: (S)ee all invoices; (E)xit")
        op = input()
        if (op == "S" or op == "s"):
            print("Invoices:")
            stmt = "SELECT nome, username FROM Client"
            cursor.execute(stmt)
            queryResult = cursor.fetchall()
            for customer in queryResult:
                print("Nome: " + customer[0] + " Username: " + customer[1])
        elif (op == "E" or op == "e"):
            sys.exit();

"""
Marketing: ver clientes / criar anuncio
Account manager: ver invoices
technical assistance: ver appliances
system manager: ver tudo
"""