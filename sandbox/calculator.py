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
PADX = 1 # padding used for buttons
PADY = 1 #

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
        #  you can also implement your own function to evalute the expression instead of 'eval' function
        result = str(eval(expression)) # 'eval' function evalutes the string expression directly
    except SyntaxError:
        # in case eval gets empty string, in case you press = one more time, it will throw SyntaxError
        btn_clear()
    else:
        # if no error, write the result on screen
        input_text.set(result)
    finally:
        # reset the expression (all the time)
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

def createButton(root, val):
    return Button(root, text=val, command = lambda: btn_click(val)) 

# creating the buttons for NUMPAD (store them in a dict for quick reference)
numpad_container = {}
for idx in range(10):
    # numpad_container[idx] = Button(btns_frame, text = str(idx), command = lambda : btn_click(idx))
    numpad_container[idx] = createButton(btns_frame, idx)
    print(numpad_container[idx]["text"])

key = 1
# placing the buttons with .grid()

for x in range(3,0,-1):
    for y in range(3):
        numpad_container[key].grid(row = x, column = y, padx = PADX, pady = PADY)
        # print("row =", x, "column =", y)
        key += 1

numpad_container[0].grid(row = 4, column = 0, columnspan = 2, padx = PADX, pady = PADY)
# see here: https://medium.com/@adeyinkaadegbenro/project-build-a-python-gui-calculator-fc92bddb744d

OPERATORS = ["C", "/", "*", "-", "+", ".", "="]
clear = Button(btns_frame, text = "C", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
plus  = Button(btns_frame, text = "+", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
point  = Button(btns_frame, text = ".", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


# tailor the buttons
for btn in btns_frame.winfo_children():
    btn_text = btn["text"]
    # NUMPAD
    if btn_text in NUMPAD:
        btn.configure(fg=FG_CLR_BTN, bg=BG_CLR_BTN, width=WIDTH_BTN, height=HEIGHT_BTN, bd=BD_BTN, cursor=CURSOR_BTN)
        if btn_text == "0": btn.configure(width=21)
    # OPERATORS
    else:
        btn.configure(fg=FG_CLR_BTN, bg=BG_CLR_BTN_OPER, width=WIDTH_BTN, height=HEIGHT_BTN, bd=BD_BTN, cursor=CURSOR_BTN)
        if btn_text == "C": btn.configure(width=32)


window.mainloop()
