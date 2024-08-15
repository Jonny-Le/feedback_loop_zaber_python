import tkinter as tk
from tkinter import messagebox

import main
import zaber_driver 

def create_gui(zaber):
    # Create the main window
    root = tk.Tk()
    root.title("Zaber Calibration Tool")

    toggle_state = [False]  # Use a list to allow modification inside the toggle function

    # State to track if the rig is currently down or up
    calibration_state = {"is_down": False}

    def toggle_calibration():
        error_label.config(text="")

        try:
            # Get the protruding value from the entry
            input_value = extruding_entry.get().strip()
            if not input_value:
                raise ValueError("Input is empty. Please enter a valid number.")
            
            # Convert input to float
            extruding_value = float(input_value)

            if calibration_state["is_down"]:
                # Move up and finish calibration
                zaber_driver.zaber_calibration(zaber, "up", 0)
                calibration_state["is_down"] = False
                calibration_button.config(text="Move Down")
            else:
                # Move down for sensor contact
                zaber_driver.zaber_calibration(zaber, "down", extruding_value)
                calibration_state["is_down"] = True
                calibration_button.config(text="Move Up")

        except ValueError as e:
            error_label.config(text=f"Invalid input: {e}. Company test rig is 22.5mm.")

    #Create the button to connect the Zaber
    #connect_button = tk.Button(root, text = "Move Down", width = 20, command = zaber_driver.zaber_connect())
    #connect_button.grid(row=0, column=0, columnspan=2, pady=20)

    # Create and place labels and entries for inputs
    tk.Label(root, text="Protruding Distance (mm):").grid(row=1, column=0, padx=5, pady=5)
    extruding_entry = tk.Entry(root)
    extruding_entry.grid(row=1, column=1, padx=5, pady=5)
    extruding_entry.insert(0, "5")  # Default value

    #Create error label for improper input 
    error_label = tk.Label(root, text="", fg="red")
    error_label.grid(row=2, column=0, columnspan=2, pady=(5, 0))

    # Create the button to start/finish calibration
    calibration_button = tk.Button(root, text = "Move Down", width = 20, command=toggle_calibration)
    calibration_button.grid(row=3, column=0, columnspan=2, pady=20)

    # Run the GUI event loop
    root.mainloop()
