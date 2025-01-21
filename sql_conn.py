#Connecting to the database

#importing 'mysql.connector' as mysql for convenient
from mysql import connector
from time import sleep

#connecting to the database using 'connect()' method
#it takes 3 required parameters 'host', 'user', 'passwd'
db = connector.connect(
	host = "moonrise6.mysql.pythonanywhere-services.com",
	user = "moonrise6",
	passwd = "z@x3!Y*N3dOx1G",
	database = "moonrise6$programmingHub"
)

print(db.is_connected()) #
print(db) # it will print a connection object if everything is fine
print('')

cursor = db.cursor()

# Delete table
cursor.execute("DROP TABLE People")
sleep(.001)

# Create table
cursor.execute("CREATE TABLE People(PName VARCHAR(50), Age INT, City VARCHAR(50))")
sleep(.001)

# Delete data
cursor.execute("DELETE FROM People")
# Insert data
cursor.execute("INSERT INTO People(PName, Age, City) VALUES "
                "('Jack', 26, 'Sydney'), "
                "('Maxi', 32, 'New York'), "
                "('John', 36, 'Mexico')")
# Update data
cursor.execute("UPDATE People SET City = 'Bogor'"
                "WHERE PName = 'John'")
db.commit()

# Execute the SELECT query
cursor.execute("SELECT * FROM People")

# Fetch the results of the SELECT query
results = cursor.fetchall()  # Fetch all rows from the result set
for row in results:
    print(row)  # Print each row (or process it as needed)

# Close the cursor
cursor.close()
db.close()