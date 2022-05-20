#to import sqlite3
import sqlite3
#to connect to the database
con= sqlite3.connect('Movie.db')
print(con) 

con.cursor()

#Inserting values into table
con.execute("INSERT INTO Movies VALUES('Life of pi','Mark ','2010','FOXCENTURY')")
con.execute("INSERT INTO Movies VALUES('zero to hero ','John ','2013','Kiran')")
con.execute("INSERT INTO Movies VALUES('15 days','Sam ','2031','Disney')")
con.execute("INSERT INTO Movies VALUES('Haloween','David','2043','Youtube')")
print("The data has been inserted into the table Movies")

#commit changes
con.commit()
con.close()
