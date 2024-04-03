import tkinter as tk


# Function to update the display when a button is clicked
def button_click(symbol):
    current = display_var.get()

    # Clear the display if the current value is 'Error'
    if current == 'Error':
        display_var.set('')

    # Update the display with the clicked symbol
    if symbol == '=':
        try:
            result = eval(current)
            display_var.set(str(result))
        except Exception as e:
            display_var.set('Error')
    elif symbol == 'C':
        display_var.set('')
    else:
        display_var.set(current + symbol)


# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Variable to store the display text
display_var = tk.StringVar()

# Create the display label
display_label = tk.Label(root, textvariable=display_var, bg="white", width=30, height=2)
display_label.place(x=30, y=20)

# Create buttons for numbers and operations
buttons = [
    ('7', 50, 100), ('8', 110, 100), ('9', 170, 100),
    ('4', 50, 160), ('5', 110, 160), ('6', 170, 160),
    ('1', 50, 220), ('2', 110, 220), ('3', 170, 220),
    ('0', 50, 280), ('.', 110, 280), ('C', 170, 280),
    ('+', 230, 100), ('-', 230, 160), ('*', 230, 220),
    ('/', 230, 280), ('=', 50, 340)
]

for btn_text, x, y in buttons:
    button = tk.Button(root, text=btn_text, width=5, height=2, command=lambda symbol=btn_text: button_click(symbol))
    button.place(x=x, y=y)

# Run the Tkinter event loop
root.mainloop()
