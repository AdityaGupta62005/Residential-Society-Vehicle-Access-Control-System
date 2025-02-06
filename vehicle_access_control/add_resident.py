# add_resident.py
import sqlite3

def add_resident(flat_number, owner_name, vehicle_number, contact_info):
    # Connect to the database
    conn = sqlite3.connect('database/society.db')
    c = conn.cursor()
    
    # Insert a new resident into the Residents table
    c.execute("INSERT INTO Residents (flat_number, owner_name, vehicle_number, contact_info) VALUES (?, ?, ?, ?)",
              (flat_number, owner_name, vehicle_number, contact_info))
    
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    print(f"Resident {owner_name} added successfully!")

if __name__ == "__main__":
    residents = [
        ("A101", "Yogita Gupta", "MH20DZ7265", "92849723"),
        ("B202", "Kunika Gupta", "MH20CW1730", "9876543210"),
        ("C303", "MK Gupta", "MH20BA1367", "9763189427"),
    ] 
    
    for resident in residents:
        add_resident(*resident)