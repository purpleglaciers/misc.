import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/Swedish top 100 frequency words - Sheet1.csv")
to_learn = data.to_dict("records")
current_card = {}
for key in current_card.keys():
    print(key, len(key))

def new_word():
    current_card = random.choice(to_learn)
    print(current_card)
    canvas.itemconfig(lang, text="Swedish")
    canvas.itemconfig(word, text=current_card["Swedish"])


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(lang, text="English")
    canvas.itemconfig(word, text=current_card["English"])



window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
window.after(3000, func=flip_card)


canvas = Canvas(height=526, width=800, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front)
lang = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

card_back = PhotoImage(file="images/card_back.png")

check_image = PhotoImage(file="images/right.png")
check_mark = Button(image=check_image, highlightbackground=BACKGROUND_COLOR, command=new_word)
check_mark.grid(row=1, column=1)

x_image = PhotoImage(file="images/wrong.png")
x_mark = Button(image=x_image, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=new_word)
x_mark.config(borderwidth=0)
x_mark.grid(row=1, column=0)


new_word()

window.mainloop()

