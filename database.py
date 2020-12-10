import mysql.connector

mydb = mysql.connector.connect(
    host="cs.holyghostprep.org/phpmyadmin/",
    user="advtopstudent",
    passwd="advtopstudent01",
)

print(mydb)
