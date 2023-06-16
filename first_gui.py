import tkinter as tk

def button_click():
    label.config(text="Button clicked!")

# Create the main window
window = tk.Tk()

# Create a label widget
label = tk.Label(window, text="Hello, GUI!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Click me!", command=button_click)
button.pack()

# Start the main event loop
window.mainloop()