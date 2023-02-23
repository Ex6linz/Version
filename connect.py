import os
import psycopg2

conn = psycopg2.connect(
    host="database",
    database="versions",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD'])

cur = conn.cursor()

#Insert versions into table

cur.execute('INSERT INTO mdp (id,version,date_time)'
            'VALUES (%s, %s, %s)'
            )



