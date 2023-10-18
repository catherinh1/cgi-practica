#!H:/INSTALADOS/PYTHON/python.exe
import mysql.connector
import os
import cgi
import cgitb
cgitb.enable()
print("Content-type: text/html\n")
print()
print("<h1>Consulta Usuarios</h1>")
print("<hr>")


con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='foro')
sql = ("SELECT *  FROM users")
cursor = con.cursor()
cursor.execute(sql)
for(email, password, name, avatar, role) in cursor:
    print("{},{},{},{},{}".format(email, password, name, avatar, role))
    print("<br>")
