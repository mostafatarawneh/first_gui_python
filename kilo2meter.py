import tkinter as tk

def convert_km_to_miles():
    km = float(km_entry.get())
    miles = km * 0.621371
    miles_label.config(text=f"Miles: {miles:.2f}")

def convert_miles_to_km():
    miles = float(miles_entry.get())
    km = miles / 0.621371
    km_label.config(text=f"Kilometers: {km:.2f}")

# Create the main window
window = tk.Tk()
window.title("Unit Converter")

# Create the kilometer to miles conversion section
km_to_miles_frame = tk.Frame(window)
km_to_miles_frame.pack(pady=10)

km_label = tk.Label(km_to_miles_frame, text="Kilometers:")
km_label.grid(row=0, column=0)

km_entry = tk.Entry(km_to_miles_frame)
km_entry.grid(row=0, column=1)

convert_button1 = tk.Button(km_to_miles_frame, text="Convert", command=convert_km_to_miles)
convert_button1.grid(row=0, column=2, padx=10)

miles_label = tk.Label(km_to_miles_frame, text="Miles: ")
miles_label.grid(row=0, column=3)

# Create the miles to kilometer conversion section
miles_to_km_frame = tk.Frame(window)
miles_to_km_frame.pack(pady=10)

miles_label2 = tk.Label(miles_to_km_frame, text="Miles:")
miles_label2.grid(row=0, column=0)

miles_entry = tk.Entry(miles_to_km_frame)
miles_entry.grid(row=0, column=1)

convert_button2 = tk.Button(miles_to_km_frame, text="Convert", command=convert_miles_to_km)
convert_button2.grid(row=0, column=2, padx=10)

km_label2 = tk.Label(miles_to_km_frame, text="Kilometers: ")
km_label2.grid(row=0, column=3)

# Start the main event loop
window.mainloop()
