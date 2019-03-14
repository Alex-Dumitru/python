from tkinter import *

# CONSTANTS

FG_CLR_BTN = 'black'
BG_CLR_BTN = 'white'
BG_CLR_BTN_OPER = '#eee'
WIDTH_BTN  = 10
HEIGHT_BTN = 3
BD_BTN = 0 # ?
CURSOR_BTN = 'hand2' # ?
NUMPAD = [str(num) for num in range(10)]

# creating basic window
window = Tk()
window.geometry("312x324") # size of the window width:- 500, height:- 375
window.resizable(0, 0) # this prevents from resizing the window
window.title("Calculator")

################################### functions ######################################
# 'btn_click' function continuously updates the input field whenever you enters a number
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'btn_clear' function clears the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# 'btn_equal' calculates the expression present in input field
def btn_equal():
    global expression
    # catch syntaxerror on eval - make action when pressing again the button
    # win calc remembers last operation and redo it
    try:
        result = str(eval(expression)) # 'eval' function evalutes the string expression directly
    except SyntaxError:
        expression = ""
    # you can also implement your own function to evalute the expression istead of 'eval' function
    input_text.set(result)
    expression = ""



expression = ""
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()


# creating a frame for the input field
input_frame = Frame(window, width = 312, height = 50, bd = 0,
highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)


# creating a input field inside the 'Frame'
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), 
                    textvariable = input_text, 
                    width = 50, 
                    bg = "#eee", 
                    bd = 0, 
                    justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10) # 'ipady' is internal padding to increase the height of input field


# creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
btns_frame.pack()


# first row
clear = Button(btns_frame, text = "C", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)


# second row
seven    = Button(btns_frame, text = "7", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight    = Button(btns_frame, text = "8", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine     = Button(btns_frame, text = "9", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)


# third row
four  = Button(btns_frame, text = "4", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five  = Button(btns_frame, text = "5", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six   = Button(btns_frame, text = "6", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)


# fourth row
one   = Button(btns_frame, text = "1", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two   = Button(btns_frame, text = "2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus  = Button(btns_frame, text = "+", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)


# fourth row
zero   = Button(btns_frame, text = "0", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point  = Button(btns_frame, text = ".", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


# tailor the NUMPAD buttons
for btn in btns_frame.winfo_children():
    btn_text = btn["text"]
    if btn_text in NUMPAD:
        btn.configure(fg=FG_CLR_BTN, bg=BG_CLR_BTN, width=WIDTH_BTN, height=HEIGHT_BTN, bd=BD_BTN, cursor=CURSOR_BTN)
        if btn_text == "0": btn.configure(width=21)
    else:
        btn.configure(fg=FG_CLR_BTN, bg=BG_CLR_BTN_OPER, width=WIDTH_BTN, height=HEIGHT_BTN, bd=BD_BTN, cursor=CURSOR_BTN)
        if btn_text == "C": btn.configure(width=32)
window.mainloop()
