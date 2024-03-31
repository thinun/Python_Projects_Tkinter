import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from gtts import gTTS


class Text_To_Speak:
    def __init__(self, root):
        self.root = root
        self.changes_done = False
        self.languages = {'English': 'en', 'French': 'fr', 'German': 'de', 'Spanish': 'es'}  # Supported languages
        self.selected_language = 'en'  # Default language is English
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Text To Speak")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        frame_1 = tk.Frame(self.root)
        frame_1.grid(row=0, column=0, sticky="ns")

        button_1 = tk.Button(frame_1, text='Open File', command=self.open_file)
        button_1.grid(row=0, column=0, sticky='ew', padx=5, pady=5)

        self.language_dropdown = ttk.Combobox(frame_1, values=list(self.languages.keys()), state='readonly')
        self.language_dropdown.current(0)  # Set the default language
        self.language_dropdown.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        self.button_2 = tk.Button(frame_1, text='Convert', command=self.save_file)
        self.button_2.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

        self.text_box = tk.Text(self.root)
        self.text_box.grid(row=0, column=1, sticky='nsew')
        self.text_box.bind('<Key>', self.check_changes)

        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Select file", filetypes=[("Text", '*.txt'), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    text = file.read()
                    self.text_box.delete(1.0, tk.END)
                    self.text_box.insert(tk.END, text)
                    self.root.title(f'Text to Speech {file_path}')
            except Exception as e:
                tk.messagebox.showerror('ERROR', f'Failed to open file: {e}')

    def save_file(self):
        file_path = filedialog.asksaveasfilename(title="Save file", filetypes=[("MP3", '*.mp3'), ("All Files", "*.*")])
        if file_path:
            try:
                output = self.text_box.get(1.0, tk.END)
                selected_language = self.languages[self.language_dropdown.get()]
                voices = gTTS(text=output, lang=selected_language, slow=False)
                voices.save(file_path)
                self.root.title(f'Text to Speech {file_path}')
                tk.messagebox.showinfo('Info', 'Text converted to speech and saved successfully!')
            except Exception as e:
                tk.messagebox.showerror('ERROR', f'Failed to save file: {e}')
        else:
            return

    def check_changes(self, event):
        self.changes_done = True

    def on_exit(self):
        if self.changes_done:
            if tk.messagebox.askyesno(title="Unsaved Changes", message="Do you want to save the changes?"):
                self.save_file()
            else:
                self.root.destroy()
        else:
            self.root.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    application = Text_To_Speak(root)
    root.mainloop()
