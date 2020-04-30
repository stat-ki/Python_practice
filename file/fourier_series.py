import tkinter as tk
import tkinter.filedialog
import math

root = tk.Tk()
root.withdraw()

filename = tkinter.filedialog.asksaveasfilename()

if filename:
    pass
else:
    print("No file specified")
    exit()

cycles = 2
steps = 1000
harmonics = 5

try:
    with open(filename, "w") as file:
        for i in range(steps):
            angle_in_degree = 360*cycles*i/steps
            angle = math.radians(angle_in_degree)
            s = str(angle_in_degree)
            w = 0
            for i in range(1, harmonics+1):
                w += math.sin(angle*(i))/i
                s = s + ", " + str(w)
            print(s)
            file.write(s + "\n")
        print("Writing file " + filename + " is finished")
except IOError:
    print("Unable to open file")