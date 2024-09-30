from tkinter import *
import math




def reset_button_clicked():
    pass


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count-1)

# After() tracks if something happened after an amount of  millisecond
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Put an image into the program. I can use the canvas() to layer things over each other.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # The image is in that size
# Get image in canvas
tomato_img = PhotoImage(file="tomato.png")  # Need to convert image
canvas.create_image(100, 112, image=tomato_img)  # First values are x and y coor
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Label

title_lable = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_lable.grid(row=0, column=1)

# CHeckmark
checkmark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
checkmark.grid(row=3, column=1)

# Buttons
start_button = Button(text="Start", command=start_countdown)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_button_clicked)
reset_button.grid(row=2, column=2)

window.mainloop()
