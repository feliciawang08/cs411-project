import sqlite3

# Connect to database
conn = sqlite3.connect('gened.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE geneds (
    Subject char(10),
    Course DATATYPE,
    CRN Datatype
)
""")