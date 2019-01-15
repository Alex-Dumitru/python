import tkinter as tk

# we create a window
window = tk.Tk()


# create a button
# first parameter for widgets should be the window object where they should go
b1 = tk.Button(window, text='Execute')
# to stick (make it appear) the button widget on the window
#b1.pack()
# second way is with grid() method. With grid you will have more control on the position
b1.grid(row=0, column=0)
# b1.grid(row=0, column=0, rowspan=2) # specify rowspan in case the widget will span on multiple rows


# entry widget
e1 = tk.Entry(window)
e1.grid(row=0, column=1)

# text widget
t1 = tk.Text(window)   # default size is quite big :P
t1 = tk.Text(window, height=1, width=20)  # change it like this
t1.grid(row=1,column=1)


# we start the window (this should be the last line)
window.mainloop()
