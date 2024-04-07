import tkinter as tk


class CalculaterGui:
    def __init__(self, root):
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        root.title("Calculator")
        root.geometry("290x370+500+200")
        root.resizable(False, False)

        # String var function to get user inputs
        self.display_variable = tk.StringVar()

        display_label = tk.Label(root, textvariable=self.display_variable, bg="white", width=25, height=2,
                                 font='Arial 12 bold',
                                 relief=tk.GROOVE)
        display_label.place(x=20, y=5)

        buttons = [
            ('(', 20, 50), (')', 85, 50), ('%', 150, 50), ('/', 215, 50),
            ('1', 20, 112), ('2', 85, 112), ('3', 150, 112), ('*', 215, 112),
            ('4', 20, 174), ('5', 85, 174), ('6', 150, 174), ('-', 215, 174),
            ('7', 20, 236), ('8', 85, 236), ('9', 150, 236), ('+', 215, 236),
            ('CR', 20, 298), ('0', 85, 298), ('.', 150, 298), ('=', 215, 298)]

        for button_value, x, y in buttons:
            button = tk.Button(root, text=button_value, font='Arial 9 bold', width=7, height=3, relief=tk.GROOVE,
                               bg='gray',
                               command=lambda symbol=button_value: self.calculator(symbol))
            button.place(x=x, y=y)

    # calculater function
    def calculator(self, symbol):
        user_input = self.display_variable.get()
        if user_input == 'ERROR':
            self.display_variable.set('')
        if symbol == '=':
            try:
                result = eval(user_input)
                self.display_variable.set(str(result))
            except Exception as e:
                self.display_variable.set('ERROR')
        elif symbol == 'CR':
            self.display_variable.set('')
        else:
            self.display_variable.set(user_input + symbol)


if __name__ == '__main__':
    root = tk.Tk()
    cal = CalculaterGui(root)
    root.mainloop()
