# **Residential Society Vehicle Access Control System**

---

## **Table of Contents**  
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Project Structure](#project-structure)  
7. [Contributing](#contributing)  
8. [License](#license)  
9. [Acknowledgements](#acknowledgements)  

---

## **Introduction**  
The **Residential Society Vehicle Access Control System** is an AI-based solution designed to automate vehicle entry and exit in residential societies. The system uses **computer vision** and **optical character recognition (OCR)** to detect and recognize vehicle number plates, verify them against a resident database, and grant or deny access accordingly. It also maintains logs of all access attempts for security and auditing purposes.

This project is developed as part of a academic project and aims to enhance security, reduce manual effort, and provide a seamless experience for residents and administrators.

---

## **Features**  
- **Real-Time Number Plate Detection**: Detects vehicle number plates from live camera feed.  
- **Text Extraction**: Uses Tesseract OCR to extract text from number plates.  
- **Database Verification**: Verifies vehicle numbers against a resident database.  
- **Access Control**: Grants or denies access based on verification results.  
- **Access Logs**: Maintains logs of all access attempts for auditing.  
- **Admin Interface**: Allows administrators to manage resident data and view logs.  

---

## **Technologies Used**  
- **Programming Language**: Python  
- **Libraries**:  
  - OpenCV (for image processing and computer vision)  
  - Tesseract OCR (for text extraction)  
  - SQLite (for database management)  
  - Tkinter (for the graphical user interface)  
- **Tools**:  
  - Git (for version control)  
  - GitHub (for project hosting)  

---

## **Installation**  
Follow these steps to set up the project on your local machine:  

### **Prerequisites**  
1. Python 3.x installed.  
2. Tesseract OCR installed on your system.  

### **Steps**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/vehicle-access-control-system.git
   cd vehicle-access-control-system
   ```

2. Install the required Python libraries:  
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:  
   - Run the `create_db.py` script to initialize the database:  
     ```bash
     python database/create_db.py
     ```

4. Start the application:  
   ```bash
   python main.py
   ```

---

## **Usage**  
1. **Live Camera Feed**:  
   - The application will display the live camera feed.  
   - Point the camera at a vehicle's number plate.  

2. **Access Control**:  
   - The system will detect the number plate, extract the text, and verify it against the resident database.  
   - Access will be granted or denied based on the verification results.  

3. **Admin Interface**:  
   - Use the admin panel to manage resident data and view access logs.  

---

## **Project Structure**  
```
vehicle-access-control-system/
├── main.py                     # Main application script
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
├── database/
│   ├── society.db              # SQLite database file
│   └── create_db.py            # Script to initialize the database
├── src/
│   ├── capture_image.py        # Module for capturing images
│   ├── preprocess_image.py     # Module for image preprocessing
│   ├── detect_number_plate.py  # Module for number plate detection
│   ├── extract_text.py         # Module for text extraction using OCR
│   ├── query_database.py       # Module for database queries
│   ├── access_control.py       # Module for access control logic
│   └── log_entry_exit.py       # Module for logging access attempts
├── ui/
│   ├── gui.py                  # Main GUI code
│   ├── styles.py               # UI styling (colors, fonts, etc.)
│   ├── widgets.py              # Custom widgets (e.g., rounded buttons)
│   └── admin_panel.py          # Admin interface for managing data
└── tests/                      # Unit tests for the project
```

---

## **Contributing**  
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:  
1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature/your-feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Add your message here"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature-name
   ```  
5. Open a pull request.  

---

## **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

## **Acknowledgements**  
- **OpenCV**: For providing powerful computer vision tools.  
- **Tesseract OCR**: For enabling accurate text extraction.  
- **SQLite**: For offering a lightweight and efficient database solution.  
- **Tkinter**: For simplifying GUI development in Python.  

---
