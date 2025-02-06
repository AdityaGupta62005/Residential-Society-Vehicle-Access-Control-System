# database/create_db.py (updated and corrected)
import sqlite3
import os

def create_database():
    # Ensure the 'database' directory exists
    os.makedirs('database', exist_ok=True)
    
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('database/society.db')
    c = conn.cursor()
    
    # Create the Residents table
    c.execute('''CREATE TABLE IF NOT EXISTS Residents
                 (id INTEGER PRIMARY KEY,
                  flat_number TEXT,
                  owner_name TEXT,
                  vehicle_number TEXT UNIQUE,
                  contact_info TEXT)''')
    
    # Create the Logs table
    c.execute('''CREATE TABLE IF NOT EXISTS Logs
                 (id INTEGER PRIMARY KEY,
                  vehicle_number TEXT,
                  status TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# def add_sample_data():
#     # Sample data to insert into the Residents table
#     sample_residents = [
#         ("A101", "John Doe", "MH01AB1234", "1234567890"),
#         ("B202", "Jane Smith", "MH02CD5678", "9876543210"),
#         ("C303", "Alice Johnson", "MH03EF9101", "5555555555"),
#     ]
    
#     # Connect to the database
#     conn = sqlite3.connect('database/society.db')
#     c = conn.cursor()
    
#     # Insert sample data
#     for resident in sample_residents:
#         flat_number, owner_name, vehicle_number, contact_info = resident
#         try:
#             c.execute("INSERT INTO Residents (flat_number, owner_name, vehicle_number, contact_info) VALUES (?, ?, ?, ?)",
#                       (flat_number, owner_name, vehicle_number, contact_info))
#             print(f"Added resident: {owner_name} (Vehicle: {vehicle_number})")
#         except sqlite3.IntegrityError:
#             print(f"Error: Vehicle number {vehicle_number} already exists in the database.")
    
#     # Commit changes and close the connection
#     conn.commit()
#     conn.close()

if __name__ == "__main__":
    # Create the database and tables
    create_database()
    print("Database initialized!")
    
    # # Optionally, add sample data
    # add_sample = input("Do you want to add sample data? (y/n): ").strip().lower()
    # if add_sample == 'y':
    #     add_sample_data()