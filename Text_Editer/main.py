import tkinter as tk
from tkinter import filedialog, messagebox


class Text_To_Speak:
    def __init__(self, root):
        self.root = root
        self.changes_done = False
        self.setup_ui()

    def setup_ui(self):

        self.root.title("Text To Speak")
        # row and column configuration

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # creating frame,button, text_box

        frame_1 = tk.Frame(self.root)
        frame_1.grid(row=0, column=0, sticky="ns")

        # button

        button_1 = tk.Button(frame_1, text='Open File', command=self.open_file)
        button_1.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        button_2 = tk.Button(frame_1, text='Save File', command=self.save_file)
        button_2.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        # text_box
        self.text_box = tk.Text(self.root)
        self.text_box.grid(row=0, column=1, sticky='nsew')

        # binding key changes to check changes function
        self.text_box.bind('<Key>', self.check_changes)

        # when exiting message box save changes or not
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select file", filetypes=[("Text", '*.txt'), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    self.text_box.delete(1.0, tk.END)
                    self.text_box.insert(tk.END, text)
                    self.root.title(f'Text to Speach {file_path}')

            except Exception as e:
                tk.messagebox.showerror('ERROR', f'Fail to open file: {e}')
        else:
            return

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title="Save file", filetypes=[("text", '*.txt'), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                output = self.text_box.get(1.0, tk.END)
                file.write(output)
                self.root.title(f'Text to Speach {file_path}')
        else:
            return

    def check_changes(self, event):
        self.changes_done = True

    def on_exit(self):
        if self.changes_done:
            if tk.messagebox.askyesno(title="Unsaved Changes", message="Do you want to save the changes"):
                self.save_file()
            else:
                self.root.destroy()
        else:
            self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    application = Text_To_Speak(root)
    root.mainloop()
