# ui/gui.py
import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import pytesseract
from src.preprocess_image import preprocess_image
from src.detect_number_plate import detect_number_plate
from src.extract_text import extract_text
from src.query_database import query_database
from ui.admin_panel import AdminPanel
from .styles import COLORS, FONTS
from .widgets import RoundedButton

class VehicleAccessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Residential Society Access Control")
        self.root.configure(bg=COLORS["background"])
        self.root.geometry("800x600")  # Set initial window size
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)
        self.is_camera_active = True
        
        # UI Setup
        self.create_widgets()
        self.update_camera_feed()

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def create_widgets(self):
        # Header Frame
        self.header_frame = ttk.Frame(self.root)
        self.header_frame.pack(fill="x", pady=10)
        
        self.title_label = ttk.Label(
            self.header_frame,
            text="Vehicle Access Control",
            font=FONTS["title"],
            foreground=COLORS["text"],
            background=COLORS["background"],
            anchor="center"
        )
        self.title_label.pack(anchor="center", pady=10)
        
        # Camera Feed Frame
        self.camera_frame = ttk.LabelFrame(self.root, text="Live Camera Feed")
        self.camera_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.camera_label = ttk.Label(self.camera_frame)
        self.camera_label.pack(anchor="center", pady=10)
        
        # Status Frame
        self.status_frame = ttk.Frame(self.root)
        self.status_frame.pack(pady=10, fill="x")
        
        self.status_label = ttk.Label(
            self.status_frame,
            text="Status: Ready",
            font=FONTS["status"],
            foreground=COLORS["text"],
            background=COLORS["background"],
            anchor="center",
            justify="center"
        )
        self.status_label.pack(anchor="center", pady=10)
        
        # Control Buttons
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(pady=10)
        
        self.admin_btn = RoundedButton(
            self.control_frame,
            text="Admin Panel",
            command=self.open_admin_panel,
            width=150,
            height=40
        )
        self.admin_btn.pack(side="left", padx=5)
        
        self.exit_btn = RoundedButton(
            self.control_frame,
            text="Exit",
            command=self.root.destroy,
            width=100,
            height=40
        )
        self.exit_btn.pack(side="left", padx=5)
    
    def update_camera_feed(self):
        try:
            if self.is_camera_active:
                ret, frame = self.cap.read()
                if ret:
                    # Detect number plate
                    processed_image = preprocess_image(frame)
                    number_plate_region = detect_number_plate(processed_image, frame)
                    
                    # Check if number_plate_region is valid
                    if number_plate_region is not None:
                        cv2.imwrite("debug_number_plate.jpg", number_plate_region)
                        print("Number plate detected!")
                        
                        vehicle_number = extract_text(number_plate_region)
                        print(f"Extracted Text: {vehicle_number}")
                        
                        # Query database
                        resident = query_database(vehicle_number)
                        self.update_status(resident, vehicle_number)
                    else:
                        print("No number plate detected.")
                    
                    # Display frame
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image=img)
                    self.camera_label.imgtk = imgtk
                    self.camera_label.configure(image=imgtk)
        except Exception as e:
            print(f"Error updating camera feed: {e}")
        
        self.root.after(10, self.update_camera_feed)
    
    def update_status(self, resident, vehicle_number):
        if resident:
            status_text = f"Access Granted: {resident[2]} (Flat {resident[1]})"
            color = COLORS["success"]
        else:
            status_text = f"Access Denied: {vehicle_number} Not Registered"
            color = COLORS["danger"]
        
        self.status_label.configure(text=status_text, foreground=color)
        self.root.update()
    
    def open_admin_panel(self):
        # Launch admin panel
        AdminPanel(tk.Toplevel(self.root))

    def on_close(self):
        """Handles application close event."""
        self.is_camera_active = False
        self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleAccessApp(root)
    root.mainloop()



# -------------------->AFTER EXIT NO. OF ENTRIES TO DISPLAY
# # ui/gui.py
# import tkinter as tk
# from tkinter import ttk
# import sqlite3
# from PIL import Image, ImageTk
# import cv2
# from .styles import COLORS, FONTS, STYLES
# from .widgets import RoundedButton
# from src.preprocess_image import preprocess_image
# from src.detect_number_plate import detect_number_plate
# from src.extract_text import extract_text
# from src.query_database import query_database

# class VehicleAccessApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Residential Society Access Control")
#         self.root.configure(bg=COLORS["background"])
#         self.root.geometry("800x600")
        
#         # Initialize camera
#         self.cap = cv2.VideoCapture(0)
#         self.is_camera_active = True
        
#         # UI Setup
#         self.create_widgets()
#         self.update_camera_feed()
    
#     def create_widgets(self):
#         # Header Frame
#         self.header_frame = ttk.Frame(self.root)
#         self.header_frame.pack(fill="x", pady=10)
        
#         self.title_label = ttk.Label(
#             self.header_frame,
#             text="Vehicle Access Control",
#             font=FONTS["title"],
#             foreground=COLORS["text"],
#             background=COLORS["background"]
#         )
#         self.title_label.pack(side="left", padx=20)
        
#         # Camera Feed Frame
#         self.camera_frame = ttk.LabelFrame(self.root, text="Live Camera Feed")
#         self.camera_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
#         self.camera_label = ttk.Label(self.camera_frame)
#         self.camera_label.pack()
        
#         # Status Frame
#         self.status_frame = ttk.Frame(self.root)
#         self.status_frame.pack(pady=10, fill="x")
        
#         self.status_label = ttk.Label(
#             self.status_frame,
#             text="Status: Ready",
#             font=FONTS["status"],
#             foreground=COLORS["text"],
#             background=COLORS["background"]
#         )
#         self.status_label.pack(side="left", padx=10)
        
#         # Control Buttons
#         self.control_frame = ttk.Frame(self.root)
#         self.control_frame.pack(pady=10)
        
#         self.admin_btn = RoundedButton(
#             self.control_frame,
#             text="Admin Panel",
#             command=self.open_admin_panel,
#             width=150,
#             height=40
#         )
#         self.admin_btn.pack(side="left", padx=5)
        
#         self.exit_btn = RoundedButton(
#             self.control_frame,
#             text="Exit",
#             command=self.show_access_logs,  # Updated command
#             width=100,
#             height=40
#         )
#         self.exit_btn.pack(side="left", padx=5)
    
#     def show_access_logs(self):
#         # Create a new window for logs
#         log_window = tk.Toplevel(self.root)
#         log_window.title("Access Logs")
#         log_window.geometry("800x400")
        
#         # Fetch granted access logs
#         conn = sqlite3.connect('database/society.db')
#         c = conn.cursor()
#         c.execute('''
#             SELECT Logs.vehicle_number, Residents.flat_number, Residents.owner_name, Logs.timestamp 
#             FROM Logs 
#             JOIN Residents ON Logs.vehicle_number = Residents.vehicle_number 
#             WHERE Logs.status = 'GRANTED'
#         ''')
#         logs = c.fetchall()
#         conn.close()
        
#         # Create a treeview to display logs
#         tree = ttk.Treeview(
#             log_window,
#             columns=("Vehicle Number", "Flat Number", "Owner", "Timestamp"),
#             show="headings"
#         )
#         tree.heading("Vehicle Number", text="Vehicle Number")
#         tree.heading("Flat Number", text="Flat Number")
#         tree.heading("Owner", text="Owner")
#         tree.heading("Timestamp", text="Timestamp")
#         tree.pack(fill="both", expand=True, padx=10, pady=10)
        
#         # Insert logs into the treeview
#         for log in logs:
#             tree.insert("", "end", values=log)
        
#         # Close button (fixed to capture log_window correctly)
#         close_btn = ttk.Button(
#             log_window,
#             text="Close and Exit",
#             command=lambda: [log_window.destroy(), self.root.destroy()]
#         )
#         close_btn.pack(pady=10)
    
#     def update_camera_feed(self):
#         if self.is_camera_active:
#             ret, frame = self.cap.read()
#             if ret:
#                 # Detect number plate
#                 processed_image = preprocess_image(frame)
#                 number_plate_region = detect_number_plate(processed_image, frame)
                
#                 if number_plate_region is not None:
#                     vehicle_number = extract_text(number_plate_region)
#                     print(f"Detected Text: {vehicle_number}")
#                     resident = query_database(vehicle_number)
#                     self.update_status(resident, vehicle_number)
                
#                 # Display frame
#                 frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 img = Image.fromarray(frame)
#                 self.imgtk = ImageTk.PhotoImage(image=img)  # Store reference
#                 self.camera_label.imgtk = self.imgtk
#                 self.camera_label.configure(image=self.imgtk)
            
#             self.root.after(10, self.update_camera_feed)
    
#     def update_status(self, resident, vehicle_number):
#         if resident:
#             status_text = f"Access Granted: {resident[2]} (Flat {resident[1]})"
#             color = COLORS["success"]
#         else:
#             status_text = f"Access Denied: {vehicle_number} Not Registered"
#             color = COLORS["danger"]
        
#         self.status_label.configure(text=status_text, foreground=color)
#         self.root.update()
    
#     def open_admin_panel(self):
#         # Launch admin panel (see next section)
#         AdminPanel(tk.Toplevel(self.root))
    
#     def __del__(self):
#         self.cap.release()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = VehicleAccessApp(root)
#     root.mainloop()