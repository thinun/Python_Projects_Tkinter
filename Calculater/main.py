import tkinter as tk

# calculater function
def calculator(symbol):
    user_input = display_variable.get()
    if user_input == 'ERROR':
        display_variable.set('')
    if symbol == '=':
        try:
            result = eval(user_input)
            display_variable.set(str(result))
        except Exception as e:
            display_variable.set('ERROR')
    elif symbol == 'CR':
        display_variable.set('')
    else:
        display_variable.set(user_input + symbol)


root = tk.Tk()
root.title("Calculator")
root.geometry("290x370+500+200")
root.resizable(False, False)

# String var function to get user inputs
display_variable = tk.StringVar()

display_label = tk.Label(root, textvariable=display_variable, bg="white", width=25, height=2, font='Arial 12 bold',
                         relief=tk.GROOVE)
display_label.place(x=20, y=5)

buttons = [
    ('(', 20, 50), (')', 85, 50), ('%', 150, 50), ('/', 215, 50),
    ('1', 20, 112), ('2', 85, 112), ('3', 150, 112), ('*', 215, 112),
    ('4', 20, 174), ('5', 85, 174), ('6', 150, 174), ('-', 215, 174),
    ('7', 20, 236), ('8', 85, 236), ('9', 150, 236), ('+', 215, 236),
    ('CR', 20, 298), ('0', 85, 298), ('.', 150, 298), ('=', 215, 298)]

for button_value, x, y in buttons:
    button = tk.Button(root, text=button_value, font='Arial 9 bold', width=7, height=3, relief=tk.GROOVE, bg='gray',
                       command=lambda symbol=button_value: calculator(symbol))
    button.place(x=x, y=y)

root.mainloop()
