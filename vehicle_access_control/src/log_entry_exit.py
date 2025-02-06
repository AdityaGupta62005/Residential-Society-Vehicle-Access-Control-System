import sqlite3

def log_entry_exit(vehicle_number, access_granted):
    conn = sqlite3.connect('database/society.db')
    c = conn.cursor()
    
    status = "GRANTED" if access_granted else "DENIED"
    c.execute("INSERT INTO Logs (vehicle_number, status) VALUES (?, ?)", (vehicle_number, status))
    
    conn.commit()
    conn.close()