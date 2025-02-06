# import cv2
# import re
# from src.preprocess_image import preprocess_image
# from src.detect_number_plate import detect_number_plate
# from src.extract_text import extract_text
# from src.query_database import query_database
# from src.access_control import access_control
# from src.log_entry_exit import log_entry_exit


# def is_valid_number_plate(text):
#     """
#     Check if the extracted text is a valid number plate.
#     A valid number plate should contain alphanumeric characters and be of a reasonable length.
#     """
#     # Example: Check for alphanumeric characters and length between 5 and 15
#     return bool(re.match(r'^[A-Za-z0-9]{5,15}$', text))

# def main():
#     # Open the laptop camera
#     cap = cv2.VideoCapture(0)
    
#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")
#             break
        
#         # Preprocess the frame
#         processed_image = preprocess_image(frame)
        
#         # Detect number plate in the frame
#         number_plate_region = detect_number_plate(processed_image, frame)
        
#         if number_plate_region is not None:
#             # Extract text from the number plate
#             vehicle_number = extract_text(number_plate_region)
#             print(f"Detected Text: {vehicle_number}")
            
#             # Check if the extracted text is a valid number plate
#             if is_valid_number_plate(vehicle_number):
#                 print(f"Valid Vehicle Number: {vehicle_number}")
                
#                 # Query the database
#                 resident = query_database(vehicle_number)
                
#                 # Control access and log event
#                 access_control(resident)
#                 log_entry_exit(vehicle_number, resident is not None)
                
#                 # Display the result on the frame
#                 if resident:
#                     cv2.putText(frame, f"Access Granted: {resident[2]} (Flat {resident[1]})", (10, 30),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#                 else:
#                     cv2.putText(frame, "Access Denied: Vehicle Not Registered", (10, 30),
#                                 cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#             else:
#                 print("Invalid number plate text. Skipping...")
        
#         # Display the frame
#         cv2.imshow("Vehicle Access Control", frame)
        
#         # Break the loop on 'q' key press
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Release the camera and close windows
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()
    
# main.py
from ui.gui import VehicleAccessApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = VehicleAccessApp(root)
    root.mainloop()    
    
# ----------->MOTION DETECTION CODE
# import cv2
# import re
# from src.preprocess_image import preprocess_image
# from src.detect_number_plate import detect_number_plate
# from src.extract_text import extract_text
# from src.query_database import query_database
# from src.access_control import access_control
# from src.log_entry_exit import log_entry_exit

# def is_valid_number_plate(text):
#     """
#     Check if the extracted text is a valid number plate.
#     A valid number plate should contain alphanumeric characters and be of a reasonable length.
#     """
#     return bool(re.match(r'^[A-Za-z0-9]{5,15}$', text))

# def main():
#     # Open the laptop camera
#     cap = cv2.VideoCapture(0)
    
#     # Initialize background subtractor for motion detection
#     fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
    
#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to capture image.")
#             break
        
#         # Apply background subtraction to detect motion
#         fgmask = fgbg.apply(frame)
        
#         # Count the number of non-zero pixels in the mask (motion area)
#         motion_pixels = cv2.countNonZero(fgmask)
        
#         # If motion is detected (above a threshold), process the frame
#         if motion_pixels > 1000:  # Adjust threshold as needed
#             print("Motion detected! Processing frame...")
            
#             # Preprocess the frame
#             processed_image = preprocess_image(frame)
            
#             # Detect number plate in the frame
#             number_plate_region = detect_number_plate(processed_image, frame)
            
#             if number_plate_region is not None:
#                 # Extract text from the number plate
#                 vehicle_number = extract_text(number_plate_region)
#                 print(f"Detected Text: {vehicle_number}")
                
#                 # Check if the extracted text is a valid number plate
#                 if is_valid_number_plate(vehicle_number):
#                     print(f"Valid Vehicle Number: {vehicle_number}")
                    
#                     # Query the database
#                     resident = query_database(vehicle_number)
                    
#                     # Control access and log event
#                     access_control(resident)
#                     log_entry_exit(vehicle_number, resident is not None)
                    
#                     # Display the result on the frame
#                     if resident:
#                         cv2.putText(frame, f"Access Granted: {resident[2]} (Flat {resident[1]})", (10, 30),
#                                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#                     else:
#                         cv2.putText(frame, "Access Denied: Vehicle Not Registered", (10, 30),
#                                     cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    
#                     # Show the frame with the result
#                     cv2.imshow("Vehicle Access Control", frame)
#                     cv2.waitKey(3000)  # Display the result for 3 seconds
#                     break  # Exit the loop after processing a valid number plate
#                 else:
#                     print("Invalid number plate text. Skipping...")
        
#         # Display the live feed (optional)
#         cv2.imshow("Vehicle Access Control", frame)
        
#         # Break the loop on 'q' key press
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
    
#     # Release the camera and close windows
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()