import tkinter as tk

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

title_entry = tk.Entry(root)
title_entry.place(x=65, y=45)

author_entry = tk.Entry(root)
author_entry.place(x=65, y=70)

isbn_entry = tk.Entry(root)
isbn_entry.place(x=65, y=95)

# buttons

view_all_button = tk.Button(root, text="View All Books")
view_all_button.place(x=250, y=20)

root.mainloop()
