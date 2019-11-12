import sqlite3
conn = sqlite3.connect("STUDENT.db")
def create():
    print("DATABASE OPENED SUCCESSFULLY\n")
    conn.execute("CREATE TABLE STUDENT1(USN TEXT PRIMARY KEY, NAME TEXT NOT NULL,SEM INT NOT NULL,CGPA FLOAT NOT NULL);")
    conn.commit()
def insert():
    conn.execute("INSERT INTO STUDENT1(USN,NAME,SEM,CGPA)VALUES('1BM18CS408','jamuna',5,8.8)")
    conn.execute("INSERT INTO STUDENT1(USN,NAME,SEM,CGPA)VALUES('1BM18CS409','lavanaya',5,8.8)")
    conn.execute("INSERT INTO STUDENT1(USN,NAME,SEM,CGPA)VALUES('1BM18CS410','madhuri',5,7.60)")
    conn.execute("INSERT INTO STUDENT1(USN,NAME,SEM,CGPA)VALUES('1BM18CS411','megha',5,8.64)")
    conn.execute("INSERT INTO STUDENT1(USN,NAME,SEM,CGPA)VALUES('1BM18CS412','meghana h l',5,8.46)")
    conn.execute("INSERT INTO STUDENT1(USN,NAME,SEM,CGPA)VALUES('1BM18CS413','nagamma',5,8.64)")
    conn.execute("INSERT INTO STUDENT1(USN,NAME,SEM,CGPA)VALUES('1BM18CS414','priyanka',5,8.64)")
    conn.commit()
def display():
    cursor = conn.execute("SELECT * FROM STUDENT1")
    print("STUDENT TABLE\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    print("\n\n")
    conn.commit()
def retrieve():
    cursor = conn.execute("SELECT * FROM STUDENT1 WHERE USN='1BM18CS421'")
    print("STUDENT WITH USN 1BM18CS421 DETAILS\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    print("\n\n")
    conn.commit()
def update():
    conn.execute("UPDATE STUDENT1 SET CGPA=7.64 WHERE USN='1BM18CS410'")
    cursor = conn.execute("SELECT * FROM STUDENT1 WHERE USN='1BM18CS410'")
    print("STUDENT WITH USN 1BM18CS410 UPDATED DETAILS\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    print("\n\n")
    conn.commit()
def delete():
    conn.execute("DELETE FROM STUDENT1 WHERE USN='1BM118CS416'")
    cursor= conn.execute("SELECT * FROM STUDENT1")
    print("UPDATED STUDENT TABLE\n")
    for row in cursor:
        print("USN =",row[0])
        print("NAME =",row[1])
        print("SEM =",row[2])
        print("CGPA =",row[3])
        print("---------------")
    conn.commit()
create()
insert()
display()
retrieve()
update()
delete()


"""
DATABASE OPENED SUCCESSFULLY

STUDENT TABLE

USN = 1BM18CS408
NAME = jamuna
SEM = 5
CGPA = 8.8
---------------
USN = 1BM18CS409
NAME = lavanaya
SEM = 5
CGPA = 8.8
---------------
USN = 1BM18CS410
NAME = madhuri
SEM = 5
CGPA = 7.6
---------------
USN = 1BM18CS411
NAME = megha
SEM = 5
CGPA = 8.64
---------------
USN = 1BM18CS412
NAME = meghana h l
SEM = 5
CGPA = 8.46
---------------
USN = 1BM18CS413
NAME = nagamma
SEM = 5
CGPA = 8.64
---------------
USN = 1BM18CS414
NAME = priyanka
SEM = 5
CGPA = 8.64
---------------



STUDENT WITH USN 1BM18CS421 DETAILS




STUDENT WITH USN 1BM18CS410 UPDATED DETAILS

USN = 1BM18CS410
NAME = madhuri
SEM = 5
CGPA = 7.64
---------------



UPDATED STUDENT TABLE

USN = 1BM18CS408
NAME = jamuna
SEM = 5
CGPA = 8.8
---------------
USN = 1BM18CS409
NAME = lavanaya
SEM = 5
CGPA = 8.8
---------------
USN = 1BM18CS410
NAME = madhuri
SEM = 5
CGPA = 7.64
---------------
USN = 1BM18CS411
NAME = megha
SEM = 5
CGPA = 8.64
---------------
USN = 1BM18CS412
NAME = meghana h l
SEM = 5
CGPA = 8.46
---------------
USN = 1BM18CS413
NAME = nagamma
SEM = 5
CGPA = 8.64
---------------
USN = 1BM18CS414
NAME = priyanka
SEM = 5
CGPA = 8.64
---------------"""
