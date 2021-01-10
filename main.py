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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0: # if it's the 1st/3rd/5th/7th rep:
        count_down(long_break_sec)
        title_label.config(text='Break', fg=RED)
    elif reps % 2 == 0: # if it's the 8th rep:
        count_down(short_break_sec)
        title_label.config(text='Break', fg=PINK)
    else: # if it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # print(count)

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count % 60}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


# label
title_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'normal'))
title_label.grid(column=1, row=0)


# pomodoro
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # allows us to layer images in window
tomato_img = PhotoImage(file='assets/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='#ffffff', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# button
start = Button(text='start', highlightthickness=0, command=start_timer)
start.config(padx=5, pady=5)
start.grid(column=0, row=2)


# label
check_marks = Label(text='✅', bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
check_marks.grid(column=1, row=3)


# button
reset = Button(text='reset', highlightthickness=0)
reset.config(padx=5, pady=5)
reset.grid(column=2, row=2)


window.mainloop()