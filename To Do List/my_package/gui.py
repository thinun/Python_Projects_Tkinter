import tkinter as tk
from pathlib import Path

from tkinter import Tk, Canvas, Button, PhotoImage

# assets linkin
ASSETS_PATH = Path(__file__).parent / "assets" / "frame0"


def relative_to_assets(path: str):
    return ASSETS_PATH / Path(path)


# user input

# user input

def create_command(check_var, task_text, check_button):
    return lambda: move_task(check_var, task_text, check_button)


def add_task():
    task_text = task_entry_widget.get()
    if task_text:
        # Add task to listbox_1
        listbox_1.insert(tk.END, task_text)

        # Create a checkbox next to the task
        check_var = tk.BooleanVar()
        check_button = tk.Checkbutton(listbox_1, bg='#1AA7EC', variable=check_var)
        check_button.config(command=create_command(check_var, task_text, check_button))

        check_button.pack(anchor=tk.E)

        # Clear the task entry
        task_entry_widget.delete(0, tk.END)


def move_task(check_var, task_text, check_button):
    if check_var.get():
        # Add task to listbox_2
        listbox_2.insert(tk.END, task_text)
        listbox_1.delete(0, tk.END)
        check_button.destroy()


window = Tk()
window.title('To-Do List')
window.geometry("478x546")
window.configure(bg='black')

canvas = Canvas(
    window,
    bg="#1AA7EC",
    height=546,
    width=478,
    bd=0,
    highlightthickness=0,
    relief="groove"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    56.0,
    172.0,
    424.0,
    527.0,
    fill="#1AA7EC",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    375.0,
    413.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    384.0,
    266.0,
    image=image_image_2
)

button_1 = Button(text='ADD', borderwidth=5, highlightthickness=2, command=add_task, relief="groove", bg='#1AA7EC')
button_1.place(
    x=336.0,
    y=150.0,
    width=73.0,
    height=37.0,

)

canvas.create_text(
    349.0,
    193.0,
    anchor="nw",
    text="ADD",
    fill="#1AA7EC",
    font=("InkFree", 20 * -1),

)

listbox_1 = tk.Listbox(bd=2, bg="#1AA7EC", fg="#000716", highlightthickness=1, font='arial 12 bold')
listbox_1.place(
    x=83.0,
    y=184.0,
    width=240.0,
    height=140.0
)

listbox_2 = tk.Listbox(bd=2, bg="#1AA7EC", fg="#000716", highlightthickness=1, font='arial 12 bold')
listbox_2.place(
    x=84.0,
    y=358.0,
    width=240.0,
    height=140.0,

)

# task entry...............................................

task_entry_widget = tk.Entry(bd=2, bg="#1AA7EC", fg="#000716", highlightthickness=0, width=26, font='arial 12 bold')
task_entry_widget.place(x=83.0, y=150.0)

canvas.create_rectangle(
    56.0,
    40.0,
    424.0,
    126.0,
    fill="#1AA7EC",
    outline="black")

canvas.create_text(
    69.0,
    57.0,
    anchor="nw",
    text="My Day",
    fill="black",
    font=("Times New Roman", 64 * -1)
)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(367.0, 85.0, image=image_image_3)

window.resizable(False, False)
window.mainloop()
