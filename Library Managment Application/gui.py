import tkinter as tk

import backend


def get_selected_row(event):
    global selected_row_id
    index = list_box.curselection()[0]
    selected_row = list_box.get(index)
    selected_row_id = selected_row[0]
    title_entry.delete(0, tk.END)
    title_entry.insert(0, selected_row[1])
    year_entry.delete(0, tk.END)
    year_entry.insert(0, selected_row[2])
    author_entry.delete(0, tk.END)
    author_entry.insert(0, selected_row[3])
    isbn_entry.delete(0, tk.END)
    isbn_entry.insert(0, selected_row[4])
    return selected_row_id


def view_command():
    list_box.delete(0, tk.END)
    data = backend.view_entries()
    for entry in data:
        list_box.insert(tk.END, entry)
    title_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    isbn_entry.delete(0, tk.END)


def search_command():
    list_box.delete(0, tk.END)
    for entry in backend.search_entry(title=title_entry.get(), author=author_entry.get(), year=year_entry.get(),
                                      isbn=isbn_entry.get()):
        list_box.insert(tk.END, str(entry))


def add_command():
    backend.add_entry(title=title_entry.get(), author=author_entry.get(), year=year_entry.get(), isbn=isbn_entry.get())
    list_box.delete(0, tk.END)
    for entry in backend.view_entries():
        list_box.insert(tk.END, entry)


def delete_command():
    backend.delete_entry(selected_row_id)
    list_box.delete(0, tk.END)
    for entry in backend.view_entries():
        list_box.insert(tk.END, entry)


def update_command():
    backend.update_entry(id=selected_row_id, title=title_entry.get(), author=author_entry.get(), year=year_entry.get(),
                         isbn=isbn_entry.get())
    list_box.delete(0, tk.END)
    for entry in backend.view_entries():
        list_box.insert(tk.END, entry)


root = tk.Tk()
root.title("Library Manager")
root.geometry("400x250")
root.resizable(width=False, height=False)

# labels
title_label = tk.Label(root, text="Title")
title_label.place(x=20, y=20)

year_label = tk.Label(root, text="Year")
year_label.place(x=20, y=45)

author_label = tk.Label(root, text="Author")
author_label.place(x=20, y=70)

isbn_label = tk.Label(root, text="ISBN")
isbn_label.place(x=20, y=95)

# entries
title_entry = tk.Entry(root)
title_entry.place(x=65, y=20)

year_entry = tk.Entry(root)  # Fixed: Separate Entry widget for Year
year_entry.place(x=65, y=45)

author_entry = tk.Entry(root)
author_entry.place(x=65, y=70)

isbn_entry = tk.Entry(root)
isbn_entry.place(x=65, y=95)

# buttons
view_all_button = tk.Button(root, text="View All Books", command=view_command)
view_all_button.place(x=200, y=20, width=85, height=25)

search_button = tk.Button(root, text="Search Entry", command=search_command)
search_button.place(x=300, y=20, width=85, height=25)

add_entry_button = tk.Button(root, text="Add Entry", command=add_command)
add_entry_button.place(x=200, y=50, width=85, height=25)

update_entry_button = tk.Button(root, text="Update Entry", command=update_command)
update_entry_button.place(x=300, y=50, width=85, height=25)

delete_entry_button = tk.Button(root, text="Delete Entry", command=delete_command)
delete_entry_button.place(x=200, y=80, width=85, height=25)

close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.place(x=300, y=80, width=85, height=25)

# scrollbar


list_box = tk.Listbox()
list_box.place(x=65, y=125, width=310, height=100)

scroll_bar = tk.Scrollbar(root)
scroll_bar.place(x=370, y=125, height=100, width=20)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

list_box.bind("<<ListboxSelect>>", get_selected_row)

root.mainloop()
