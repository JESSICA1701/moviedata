#to import sqlite3
import sqlite3

con = sqlite3.connect('Movie.db')
cur = con.cursor()

#run query to show all the movies details
cursor = cur.execute("SELECT * FROM Movies")
print(cur.fetchall())

# Query to fetch only movie name
cur.execute("SELECT MovieName From Movies ")
print(cur.fetchall())

con.commit()
con.close()
