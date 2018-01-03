import MySQLdb

db = MySQLdb.connect (host ="192.168.1.107",user = "falcon",passwd = "Falcon->123",db = "employees")
cursor =db.cursor()
cursor.execute("SELECT * from departments")
for row in cursor.fetchall() :
    print (row[0], " ", row[1])

