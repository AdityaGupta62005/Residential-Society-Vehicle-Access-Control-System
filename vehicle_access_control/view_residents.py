# view_residents.py
import sqlite3

def view_residents():
    # Connect to the database
    conn = sqlite3.connect('database/society.db')
    c = conn.cursor()
    
    # Fetch all records from the Residents table
    c.execute("SELECT * FROM Residents")
    residents = c.fetchall()
    
    # Print the records
    for resident in residents:
        print(resident)
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    view_residents()