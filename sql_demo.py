import psycopg2

conn = psycopg2.connect(host='localhost', user='falcon', password='9929EvxP', database='falcon')

cur = conn.cursor()

cur.execute('select * from playground')

for item in cur.fetchall():
    print(item)


cur.close()


