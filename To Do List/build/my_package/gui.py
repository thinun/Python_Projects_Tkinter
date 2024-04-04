from pathlib import Path


from tkinter import Tk, Canvas, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\TT\1 Python Journey\Python Projects(Tkinter)\To Do List\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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

button_1 = Button(
    text='ADD',
    borderwidth=5,
    highlightthickness=2,
    command=lambda: print("button_1 clicked"),
    relief="groove",
    bg='#1AA7EC'

)
button_1.place(
    x=336.0,
    y=181.0,
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


entry_1 = Text(
    bd=2,
    bg="#1AA7EC",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=83.0,
    y=184.0,
    width=240.0,
    height=155.0
)


entry_2 = Text(
    bd=2,
    bg="#1AA7EC",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=84.0,
    y=358.0,
    width=240.0,
    height=140.0,

)

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
    font=("InkFree", 64 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    367.0,
    85.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
