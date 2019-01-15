import tkinter as tk

# create the window object
window = tk.Tk()

# define the function
def kg_conv():
    grams = float(e1_value.get()) * 1000   # convert kg to grams
    pounds = float(e1_value.get()) * 2.20462   # convert kg to pounds
    ounces = float(e1_value.get()) * 35.274   # convert kg to ounces
    # insert the values in respective fields
    t1.insert(tk.END,grams)
    t2.insert(tk.END,pounds)
    t3.insert(tk.END,ounces)

# Create the button
b1 = tk.Button(window, text='Convert', command=kg_conv)
b1.grid(row=0, column=3)

# Create the entry text field
e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=2)

# Create the text widgets to display the results
t1 = tk.Text(window, height=1, width=20)
t1.grid(row=1,column=1)
t2 = tk.Text(window, height=1, width=20)
t2.grid(row=1,column=2)
t3 = tk.Text(window, height=1, width=20)
t3.grid(row=1,column=3)

# Create a label to display input data type
l1 = tk.Label(window, justify='center', text='KG')
l1.grid(row=0, column=0)
window.mainloop()
