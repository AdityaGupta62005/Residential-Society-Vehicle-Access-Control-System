def access_control(resident):
    if resident:
        print(f"Access granted to {resident[2]} (Flat {resident[1]})")
    else:
        print("Access denied: Vehicle not registered.")