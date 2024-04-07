import tkinter as tk

import backend

selected_row_id = None


class Application:
    def __init__(self, root):
        self.root = root
        self.selected_row_id = None
        self.setup_gui()

    def setup_gui(self):
        root.title("Library Manager")
        root.geometry("400x250")
        root.resizable(width=False, height=False)

        # labels
        self.title_label = tk.Label(root, text="Title")
        self.title_label.place(x=20, y=20)

        self.year_label = tk.Label(root, text="Year")
        self.year_label.place(x=20, y=45)

        self.author_label = tk.Label(root, text="Author")
        self.author_label.place(x=20, y=70)

        self.isbn_label = tk.Label(root, text="ISBN")
        self.isbn_label.place(x=20, y=95)

        # entries
        self.title_entry = tk.Entry(root)
        self.title_entry.place(x=65, y=20)

        self.year_entry = tk.Entry(root)  # Fixed: Separate Entry widget for Year
        self.year_entry.place(x=65, y=45)

        self.author_entry = tk.Entry(root)
        self.author_entry.place(x=65, y=70)

        self.isbn_entry = tk.Entry(root)
        self.isbn_entry.place(x=65, y=95)

        # buttons
        self.view_all_button = tk.Button(root, text="View All Books", command=self.view_command)
        self.view_all_button.place(x=200, y=20, width=85, height=25)

        self.search_button = tk.Button(root, text="Search Entry", command=self.search_command)
        self.search_button.place(x=300, y=20, width=85, height=25)

        self.add_entry_button = tk.Button(root, text="Add Entry", command=self.add_command)
        self.add_entry_button.place(x=200, y=50, width=85, height=25)

        self.update_entry_button = tk.Button(root, text="Update Entry", command=self.update_command)
        self.update_entry_button.place(x=300, y=50, width=85, height=25)

        self.delete_entry_button = tk.Button(root, text="Delete Entry", command=self.delete_command)
        self.delete_entry_button.place(x=200, y=80, width=85, height=25)

        self.close_button = tk.Button(root, text="Close", command=root.destroy)
        self.close_button.place(x=300, y=80, width=85, height=25)

        # scrollbar

        self.list_box = tk.Listbox()
        self.list_box.place(x=65, y=125, width=310, height=100)

        self.scroll_bar = tk.Scrollbar(root)
        self.scroll_bar.place(x=370, y=125, height=100, width=20)

        self.list_box.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(command=self.list_box.yview)

        self.list_box.bind("<<ListboxSelect>>", self.get_selected_row)

    def get_selected_row(self, event):
        global selected_row_id
        index = self.list_box.curselection()[0]
        selected_row = self.list_box.get(index)
        selected_row_id = selected_row[0]
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, selected_row[1])
        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, selected_row[2])
        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(0, selected_row[3])
        self.isbn_entry.delete(0, tk.END)
        self.isbn_entry.insert(0, selected_row[4])
        return selected_row_id

    def view_command(self):
        self.list_box.delete(0, tk.END)
        data = backend.view_entries()
        for entry in data:
            self.list_box.insert(tk.END, entry)
        self.title_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)

    def search_command(self):
        self.list_box.delete(0, tk.END)
        for entry in backend.search_entry(title=self.title_entry.get(), author=self.author_entry.get(),
                                          year=self.year_entry.get(),
                                          isbn=self.isbn_entry.get()):
            self.list_box.insert(tk.END, str(entry))

    def add_command(self):
        backend.add_entry(title=self.title_entry.get(), author=self.author_entry.get(), year=self.year_entry.get(),
                          isbn=self.isbn_entry.get())
        self.list_box.delete(0, tk.END)
        for entry in backend.view_entries():
            self.list_box.insert(tk.END, entry)

    def delete_command(self):
        backend.delete_entry(selected_row_id)
        self.list_box.delete(0, tk.END)
        for entry in backend.view_entries():
            self.list_box.insert(tk.END, entry)

    def update_command(self):
        backend.update_entry(id=selected_row_id, title=self.title_entry.get(), author=self.author_entry.get(),
                             year=self.year_entry.get(),
                             isbn=self.isbn_entry.get())
        self.list_box.delete(0, tk.END)
        for entry in backend.view_entries():
            self.list_box.insert(tk.END, entry)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
