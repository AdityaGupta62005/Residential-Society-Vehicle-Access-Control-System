# ui/admin_panel.py
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from .styles import COLORS, FONTS

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Panel")
        self.root.configure(bg=COLORS["background"])
        
        self.create_widgets()
        self.load_residents()
    
    def create_widgets(self):
        # Resident List
        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Flat", "Owner", "Vehicle", "Contact"),
            show="headings"
        )
        self.tree.heading("ID", text="ID")
        self.tree.heading("Flat", text="Flat Number")
        self.tree.heading("Owner", text="Owner Name")
        self.tree.heading("Vehicle", text="Vehicle Number")
        self.tree.heading("Contact", text="Contact Info")
        self.tree.pack(pady=10, padx=10, fill="both", expand=True)
        
        # Add/Edit Form
        self.form_frame = ttk.Frame(self.root)
        self.form_frame.pack(pady=10, fill="x")
        
        ttk.Label(self.form_frame, text="Flat Number:").grid(row=0, column=0, padx=5)
        self.flat_entry = ttk.Entry(self.form_frame)
        self.flat_entry.grid(row=0, column=1, padx=5)
        
        ttk.Label(self.form_frame, text="Owner Name:").grid(row=0, column=2, padx=5)
        self.owner_entry = ttk.Entry(self.form_frame)
        self.owner_entry.grid(row=0, column=3, padx=5)
        
        ttk.Label(self.form_frame, text="Vehicle Number:").grid(row=1, column=0, padx=5)
        self.vehicle_entry = ttk.Entry(self.form_frame)
        self.vehicle_entry.grid(row=1, column=1, padx=5)
        
        ttk.Label(self.form_frame, text="Contact Info:").grid(row=1, column=2, padx=5)
        self.contact_entry = ttk.Entry(self.form_frame)
        self.contact_entry.grid(row=1, column=3, padx=5)
        
        self.add_btn = ttk.Button(
            self.form_frame,
            text="Add/Update Resident",
            command=self.save_resident
        )
        self.add_btn.grid(row=2, column=0, columnspan=4, pady=10)
    
    def load_residents(self):
        conn = sqlite3.connect('database/society.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Residents")
        residents = c.fetchall()
        conn.close()
        
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        for resident in residents:
            self.tree.insert("", "end", values=resident)
    
    def save_resident(self):
        flat = self.flat_entry.get()
        owner = self.owner_entry.get()
        vehicle = self.vehicle_entry.get()
        contact = self.contact_entry.get()
        
        conn = sqlite3.connect('database/society.db')
        c = conn.cursor()
        try:
            c.execute(
                "INSERT OR REPLACE INTO Residents (flat_number, owner_name, vehicle_number, contact_info) VALUES (?, ?, ?, ?)",
                (flat, owner, vehicle, contact)
            )
            conn.commit()
            messagebox.showinfo("Success", "Resident data saved!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Vehicle number already exists!")
        finally:
            conn.close()
            self.load_residents()