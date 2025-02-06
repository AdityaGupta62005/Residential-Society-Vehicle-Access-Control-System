import sqlite3

def query_database(vehicle_number):
    conn = sqlite3.connect('database/society.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM Residents WHERE vehicle_number=?", (vehicle_number,))
    result = c.fetchone()
    
    conn.close()
    return result
