import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_equation():
    equation = equation_entry.get()
    x_range = (float(x_min_entry.get()), float(x_max_entry.get()))

    x = np.linspace(x_range[0], x_range[1], 100)
    y = eval(equation)

    fig = plt.figure()
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph of ' + equation)
    plt.grid(True)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# لعمل الشاشه
window = tk.Tk()
window.title("Equation Graphing")

# استقبال المعادله
equation_label = tk.Label(window, text="Equation:")
equation_label.pack()
equation_entry = tk.Entry(window)
equation_entry.pack()

# محور الاكس input
x_range_label = tk.Label(window, text="X-range:")
x_range_label.pack()
x_min_entry = tk.Entry(window)
x_min_entry.pack(side=tk.LEFT)
x_max_entry = tk.Entry(window)
x_max_entry.pack(side=tk.RIGHT)

# هنا عمل الفريم الذي يتم فيه الرسم
graph_frame = tk.Frame(window)
graph_frame.pack()

# زر الرسم
plot_button = tk.Button(window, text="Plot", command=plot_equation)
plot_button.pack()

# تشغيل البرنامج
window.mainloop()
