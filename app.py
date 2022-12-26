import copy
from getpass import getpass
import sys
import mysql.connector
import hashlib

def allContracts():
    print("Contractos:")
    stmt = "SELECT id, tipo FROM Contract"
    cursor.execute(stmt)
    queryResult = cursor.fetchall()
    for contract in queryResult:
        print("ID: " + str(contract[0]) + " // Tipo: " + contract[1])

def allCustomers():
    print("Clientes:")
    stmt = "SELECT id,nome,username FROM Client"
    cursor.execute(stmt)
    queryResult = cursor.fetchall()
    for customer in queryResult:
        print("ID: " + str(customer[0]) + " // Name: " + customer[1] + " // Username: " + customer[2])

def createAppliance():
    nome = input("Insert the appliance's name:")
    maxConsumption = input("Insert the appliance's maxConsumption:")
    isProducing = input("Is the appliance producing?: (TRUE/FALSE) ")
    allContracts()
    contractID = input("Insert the contract's ID:")
    allCustomers()
    clientID = input("Insert the client's ID:")
    stmt = "INSERT INTO Appliance (nome, maxConsumption, isProducing, contractID, clientID) VALUES ('" + nome + "', " + maxConsumption + ", " + isProducing + ", " + contractID + ", " + clientID + ")"
    cursor.execute(stmt)
    cnx.commit()
    
def createAdd():
    addContent = input("Insert the Add content:")
    stmt = "INSERT INTO Adds (content) VALUES '" + addContent + "'"
    cursor.execute(stmt)

def allApliances():
    print("Appliances:")
    stmt = "SELECT nome, isProducing FROM Appliance"
    cursor.execute(stmt)
    queryResult = cursor.fetchall()
    for appliance in queryResult:
        print("Name: " + appliance[0] + " // Produces Energy?: " + str(appliance[1]))

def allInvoices():
    print("Invoices:")


cnx = mysql.connector.connect(user='seed', password='deesdees',
                              host='localhost',
                              database='remotedb')
cursor = cnx.cursor(prepared = True)

print("----------- Welcome to ECOGES back-office ----------\n" + 
"Please insert your login credentials:")
username = input("Username:")
password = getpass()
stmt = "SELECT nome, roleID FROM Employee WHERE username = %s and password = %s"
password = hashlib.sha512(password.encode("utf-8")).hexdigest()
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
           allCustomers()
        elif (op == "C" or op == "c"):
            createAdd()
        elif (op == "E" or op == "e"):
            sys.exit();
elif (role == "Account Manager"):
    while (True):
        print("Operations: (S)ee all invoices; (E)xit")
        op = input()
        if (op == "S" or op == "s"):
            allInvoices()
        elif (op == "E" or op == "e"):
            sys.exit();
elif (role == "Technical Assistant"):
    while (True):
        print("Operations: (S)ee all appliances; (E)xit")
        op = input()
        if (op == "S" or op == "s"):
            allApliances()
        elif (op == "E" or op == "e"):
            sys.exit();
elif (role == "System Manager"):
    while (True):
        print("Operations: (SA) See all appliances; (SC) See all clients; (SI) See all invoices; (C)reate Appliance; (E)xit")
        op = input()
        if (op == "SA" or op == "sa"):
            allApliances()
        elif (op == "SC" or op == "sc"):
            allCustomers()
        elif (op == "SI" or op == "si"):
            allInvoices()
        elif (op == "C" or op == "c"):
            createAppliance()
        elif (op == "E" or op == "e"):
            sys.exit();



"""
Marketing: ver clientes / criar anuncio
Account manager: ver invoices
technical assistance: ver appliances
system manager: ver tudo
"""