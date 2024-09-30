from tkinter import *
import math


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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st/3rd/5th/7th rep:
    if reps % 8 == 0:
        title_lable.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # If it's 8th rep:
    elif reps % 2 == 0:
        title_lable.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # If it's 2nd/4th/6th rep:
    else:
        title_lable.config(text="Work")
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    global reps

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_countdown()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


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

# Checkmark
checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
checkmark.grid(row=3, column=1)

# Buttons
start_button = Button(text="Start", command=start_countdown)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
