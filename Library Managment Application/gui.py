import tkinter as tk
import backend



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
view_all_button = tk.Button(root, text="View All Books")
view_all_button.place(x=200, y=20, width=85, height=25)

search_button = tk.Button(root, text="Search Entry")
search_button.place(x=300, y=20, width=85, height=25)

add_entry_button = tk.Button(root, text="Add Entry")
add_entry_button.place(x=200, y=50, width=85, height=25)

update_entry_button = tk.Button(root, text="Update Entry")  # Fixed: Updated button name
update_entry_button.place(x=300, y=50, width=85, height=25)

delete_entry_button = tk.Button(root, text="Delete Entry")
delete_entry_button.place(x=200, y=80, width=85, height=25)

close_button = tk.Button(root, text="Close")
close_button.place(x=300, y=80, width=85, height=25)

# scrollbar


list_box = tk.Listbox()
list_box.place(x=65, y=125, width=310, height=100)

scroll_bar = tk.Scrollbar(root)
scroll_bar.place(x=370, y=125, height=100, width=20)

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

root.mainloop()
