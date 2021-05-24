import tkinter as tk

window = tk.Tk()

#result label
lbl_result = tk.Label(master=window)
lbl_result.grid(row=5, columnspan=4)

expression = ''

def press(char):
    # lbl_result['text'] = number
    global expression
    expression = expression + char
    lbl_result['text'] = expression

def equal():
    global expression
    lbl_result['text'] = str(eval(expression))
    expression = str(eval(expression))

def clear():
    global expression
    expression = ''
    lbl_result['text'] = expression

#number buttons
btn_0 = tk.Button(master=window, text = '0', width=5, height=5, command = lambda: press('0'))
btn_0.grid(row=4, column=2)
btn_1 = tk.Button(master=window, text = '1', width=5, height=5, command = lambda: press('1'))
btn_1.grid(row=1, column=1)
btn_2 = tk.Button(master=window, text = '2', width=5, height=5, command = lambda: press('2'))
btn_2.grid(row=1, column=2)
btn_3 = tk.Button(master=window, text = '3', width=5, height=5, command = lambda: press('3'))
btn_3.grid(row=1, column=3)
btn_4 = tk.Button(master=window, text = '4', width=5, height=5, command = lambda: press('4'))
btn_4.grid(row=2, column=1)
btn_5 = tk.Button(master=window, text = '5', width=5, height=5, command = lambda: press('5'))
btn_5.grid(row=2, column=2)
btn_6 = tk.Button(master=window, text = '6', width=5, height=5, command = lambda: press('6'))
btn_6.grid(row=2, column=3)
btn_7 = tk.Button(master=window, text = '7', width=5, height=5, command = lambda: press('7'))
btn_7.grid(row=3, column=1)
btn_8 = tk.Button(master=window, text = '8', width=5, height=5, command = lambda: press('8'))
btn_8.grid(row=3, column=2)
btn_9 = tk.Button(master=window, text = '9', width=5, height=5, command = lambda: press('9'))
btn_9.grid(row=3, column=3)

#operation buttons
btn_plus = tk.Button(master=window, text = '+', width=5, height=5, command = lambda: press('+'))
btn_plus.grid(row=1, column=4)
btn_minus = tk.Button(master=window, text = '-', width=5, height=5, command = lambda: press('-'))
btn_minus.grid(row=2, column=4)
btn_multiply = tk.Button(master=window, text = '*', width=5, height=5, command = lambda: press('*'))
btn_multiply.grid(row=3, column=4)
btn_divide = tk.Button(master=window, text = '/', width=5, height=5, command = lambda: press('/'))
btn_divide.grid(row=4, column=4)
btn_equal = tk.Button(master=window, text = '=', width=5, height=5, command = equal)
btn_equal.grid(row=4, column=3)
btn_clear = tk.Button(master=window, text = 'C', width=5, height=5, command = clear)
btn_clear.grid(row=4, column=1)

window.mainloop()
