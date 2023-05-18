import mysql.connector

# Connect to the MySQL server
cnx = mysql.connector.connect(user='abhi', password='abhi',
                              host='127.0.0.1')

# Create a new database
db_cursor = cnx.cursor()
db_cursor.execute("CREATE DATABASE coaching_institute")
db_cursor.close()

# Connect to the new database
cnx = mysql.connector.connect(user='abhi', password='abhi',
                              host='127.0.0.1', database='coaching_institute')

# Create a new table
table_cursor = cnx.cursor()
table_cursor.execute("CREATE TABLE students ("
                     "id INT AUTO_INCREMENT PRIMARY KEY,"
                     "name VARCHAR(255) NOT NULL,"
                     "class VARCHAR(10) NOT NULL,"
                     "address VARCHAR(255) NOT NULL,"
                     "fee_paid DECIMAL(10,2) NOT NULL,"
                     "fee_pending DECIMAL(10,2) NOT NULL"
                     ")")
table_cursor.close()

# Close the database connection

