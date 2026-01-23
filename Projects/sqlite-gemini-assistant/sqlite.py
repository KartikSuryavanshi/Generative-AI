import sqlite3


## connect to the SQLite database
connection= sqlite3.connect('students.db')

# create a cursor object to insert records,create tables,fetch records
cursor= connection.cursor()

## create a table
table_info= """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));
"""

cursor.execute(table_info)


## insert records into the table
cursor.execute(''' Insert into STUDENT(NAME,CLASS,SECTION) values('Kartik Suryavanshi','DS','A') ''')
cursor.execute(''' Insert into STUDENT(NAME,CLASS,SECTION) values('Sammer Patil','DA','B') ''')
cursor.execute(''' Insert into STUDENT(NAME,CLASS,SECTION) values('Rahul Kumar','DS','A') ''')
cursor.execute(''' Insert into STUDENT(NAME,CLASS,SECTION) values('Priya Singh','DA','C') ''')
cursor.execute(''' Insert into STUDENT(NAME,CLASS,SECTION) values('Amit Sharma','DS','B') ''')

## DISPLAY RECORDS
print("The inserted records are: ")
data = cursor.execute(''' Select * from STUDENT ''')
for row in data:
    print(row)