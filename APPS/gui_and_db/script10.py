import tkinter as tk

window = tk.Tk()

def km_to_miles():
    print('Success!')
    print(e1_value.get())  # here we use the get() method of the object, to get the value stored
    # to insert the value in the text widget, you need to refer to the one that you want (t1) and use its speficit method
    # 1st arg of the insert method is the place where you want to insert the text
    miles = float(e1_value.get()) * 1.6   # convert km to miles
    #t1.insert(tk.END,e1_value.get())
    t1.insert(tk.END,miles)

# to make a button do something, we need to add the command parameter which takes a function as the value
# you do not pass the function with ()
b1 = tk.Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0, column=0)

# to get the value from the Entry widget, we use textvariable param which is equal to a StringVar object
e1_value = tk.StringVar()
e1 = tk.Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = tk.Text(window, height=1, width=20)
t1.grid(row=1,column=1)


window.mainloop()
