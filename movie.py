# to import sqlite3 module
import sqlite3

#to connect with database
con= sqlite3.connect('Movie.db')
print(con)
cur = con.cursor()

#to create table name Movies
cur.execute('CREATE TABLE IF NOT EXISTS Movies(MovieName VARCHAR,ActorName VARCHAR,YearOfRelease INT,Director VARCHAR)')
print('Movies table has been created in Movie database')

#to commit changes
con.commit()
#to close connection
con.close()
