import tkinter as tk
import re


def get_data():
    user_input = entry1.get()

    # Validate input: check if the input contains only numbers and operators
    if re.match(r'^[0-9+*/%().\s-]*$', user_input):
        try:
            result = eval(user_input)
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, str(result))
        except Exception as e:
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, "Error")
    else:
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, "Invalid Input")


def validate_input(*args):
    current_value = entry1.get()
    filtered_value = re.sub(r'[^0-9+*/%().\s-]', '', current_value)
    if current_value != filtered_value:
        entry1.delete(0, tk.END)
        entry1.insert(tk.END, filtered_value)


# input button functions
def one():
    entry1.insert(tk.END, '1')


def two():
    entry1.insert(tk.END, '2')


def three():
    entry1.insert(tk.END, '3')


def four():
    entry1.insert(tk.END, '4')


def five():
    entry1.insert(tk.END, '5')


def six():
    entry1.insert(tk.END, '6')


def seven():
    entry1.insert(tk.END, '7')


def eight():
    entry1.insert(tk.END, '8')


def nine():
    entry1.insert(tk.END, '9')


def zero():
    entry1.insert(tk.END, '0')


def clear():
    entry1.delete(0, tk.END)


def open_bracket():
    entry1.insert(tk.END, '(')


def closing_bracket():
    entry1.insert(tk.END, ')')


def percentage():
    entry1.insert(tk.END, '%')


def divide():
    entry1.insert(tk.END, '/')


def multiply():
    entry1.insert(tk.END, '*')


def subtract():
    entry1.insert(tk.END, '-')


def add():
    entry1.insert(tk.END, '+')


root = tk.Tk()
root.title("Calculator")
root.geometry("250x300+500+100")
root.resizable(False, False)

entry1 = tk.Entry(root, width=21, font="Arial 15 bold")
entry1.place(x=10, y=0)

# Bind key press event to validate input
entry1.bind('<KeyRelease>', validate_input)

# buttons
button1 = tk.Button(text='(', padx=20, pady=10, width=1, height=1, command=open_bracket)
button1.place(x=10, y=40)
button2 = tk.Button(text=')', padx=20, pady=10, width=1, height=1, command=closing_bracket)
button2.place(x=70, y=40)
button3 = tk.Button(text='%', padx=20, pady=10, width=1, height=1, command=percentage)
button3.place(x=130, y=40)
button4 = tk.Button(text='/', padx=20, pady=10, width=1, height=1, command=divide)
button4.place(x=190, y=40)

button5 = tk.Button(text='1', padx=20, pady=10, width=1, height=1, command=one)
button5.place(x=10, y=90)
button6 = tk.Button(text='2', padx=20, pady=10, width=1, height=1, command=two)
button6.place(x=70, y=90)
button7 = tk.Button(text='3', padx=20, pady=10, width=1, height=1, command=three)
button7.place(x=130, y=90)
button8 = tk.Button(text='*', padx=20, pady=10, width=1, height=1, command=multiply)
button8.place(x=190, y=90)

button9 = tk.Button(text='4', padx=20, pady=10, width=1, height=1, command=four)
button9.place(x=10, y=140)
button10 = tk.Button(text='5', padx=20, pady=10, width=1, height=1, command=five)
button10.place(x=70, y=140)
button11 = tk.Button(text='6', padx=20, pady=10, width=1, height=1, command=six)
button11.place(x=130, y=140)
button12 = tk.Button(text='-', padx=20, pady=10, width=1, height=1, command=subtract)
button12.place(x=190, y=140)

button13 = tk.Button(text='7', padx=20, pady=10, width=1, height=1, command=seven)
button13.place(x=10, y=190)
button14 = tk.Button(text='8', padx=20, pady=10, width=1, height=1, command=eight)
button14.place(x=70, y=190)
button15 = tk.Button(text='9', padx=20, pady=10, width=1, height=1, command=nine)
button15.place(x=130, y=190)
button16 = tk.Button(text='+', padx=20, pady=10, width=1, height=1, command=add)
button16.place(x=190, y=190)

button17 = tk.Button(text='CR', padx=20, pady=10, width=1, height=1, command=clear)
button17.place(x=10, y=240)
button18 = tk.Button(text='0', padx=20, pady=10, width=1, height=1, command=zero)
button18.place(x=70, y=240)
button19 = tk.Button(text='.', padx=20, pady=10, width=1, height=1, command=lambda: entry1.insert(tk.END, '.'))
button19.place(x=130, y=240)
button20 = tk.Button(text='=', padx=20, pady=10, width=1, height=1, command=get_data)
button20.place(x=190, y=240)

root.mainloop()
