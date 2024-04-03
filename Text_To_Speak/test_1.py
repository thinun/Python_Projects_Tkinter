import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import pyttsx3
from gtts import gTTS


class Text_To_Speak:
    def __init__(self, root):
        self.root = root
        self.changes_done = False
        self.engine = pyttsx3.init()
        self.language_mapping = {
            'English': 'en',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Spanish': 'es',
            'Portuguese': 'pt',
            'Russian': 'ru',
            'Japanese': 'ja',
            'Hindi': 'hi',
            'Korean': 'ko',
            'Chinese': 'zh',
            'Arabic': 'ar',
            'Dutch': 'nl',
            'Turkish': 'tr',
            'Polish': 'pl',
            'Swedish': 'sv',
            'Danish': 'da',
            'Norwegian': 'no',
            'Finnish': 'fi',
            'Greek': 'el',
            'Czech': 'cs',
            'Hungarian': 'hu',
            'Romanian': 'ro',
            'Catalan': 'ca',
            'Vietnamese': 'vi',
            'Thai': 'th',
            'Indonesian': 'id',
            'Slovak': 'sk',
            'Croatian': 'hr',
            'Bulgarian': 'bg',
            'Serbian': 'sr',
            'Ukrainian': 'uk',
            'Malay': 'ms',
            'Hebrew': 'he',
            'Bengali': 'bn',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Kannada': 'kn',
            'Marathi': 'mr',
            'Gujarati': 'gu',
            'Sinhala': 'si',
            'Urdu': 'ur'
        }

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

        self.dropdown = ttk.Combobox(frame_1, values=list(self.language_mapping.keys()), state='readonly')
        self.dropdown.current(0)
        self.dropdown.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        button_2 = tk.Button(frame_1, text='Convert', command=self.save_file)
        button_2.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

        self.dropdown_0 = ttk.Combobox(frame_1, values=list(['Male', 'Female']), state='readonly')
        self.dropdown_0.current(0)
        self.dropdown_0.grid(row=3, column=0, sticky='ew', padx=5, pady=5)

        button_3 = tk.Button(frame_1, text='Speak', command=self.speak)
        button_3.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

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
        file_path = filedialog.asksaveasfilename(title="Save file", filetypes=[("mp3", '*.mp3'), ("All Files", "*.*")])
        if file_path:
            try:
                output = self.text_box.get(1.0, tk.END)
                select_language = self.language_mapping[self.dropdown.get()]
                voices = gTTS(text=output, lang=select_language, slow=False)
                voices.save(f'{file_path}.mp3')
                self.root.title(f'Text to Speach {file_path}')
                tk.messagebox.showinfo('Success', 'Text to Speach Conversion Complete!')

            except Exception as e:
                tk.messagebox.showerror('ERROR', f'Fail to Convert: {e}')

        else:
            return

    def check_changes(self, event):
        self.changes_done = True

    def on_exit(self):
        self.engine.stop()
        if self.changes_done:
            if tk.messagebox.askyesno(title="Unsaved Changes", message="Do you want to save the changes"):
                self.save_file()
            else:
                self.root.destroy()
        else:
            self.root.destroy()

    def speak(self):

        voices = self.engine.getProperty('voices')
        select_voice = self.dropdown_0.get().lower()
        if select_voice == "male":
            self.engine.setProperty('voice', voices[0].id)

        elif select_voice == "female":
            self.engine.setProperty('voice', voices[1].id)

        data = self.text_box.get(1.0, tk.END)

        speech_thread = threading.Thread(target=self.run_speech, args=(data,))
        speech_thread.start()

    def run_speech(self, data):
        self.engine.say(data)
        self.engine.runAndWait()


if __name__ == '__main__':
    root = tk.Tk()

    application = Text_To_Speak(root)
    root.mainloop()
