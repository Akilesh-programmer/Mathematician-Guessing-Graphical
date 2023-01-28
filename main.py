from names import word_list
from tkinter import *
import random
from tkinter import messagebox

lives = 10

# Choosing random name
rand_int = random.randint(0, len(word_list) - 1)
chosen_name = word_list[rand_int]

x_size = len(chosen_name) * 65 + 50

# Window
root = Tk()
# bgimg = PhotoImage(file="Math-Wallpaper.jpg")
# limg = Label(root, i=bgimg)
root.geometry(f'{x_size}x400')
root.title("Guess The Name")
root.resizable(False, False)
root.configure(bg="#E6624C")

# Function for using "Enter" key as submit
root.bind('<Return>', lambda event: get_input())

# Icon
icon = PhotoImage(file="speech-bubble.png")
root.iconphoto(False, icon)

# Labels
labels = []
for i in chosen_name:
    label = Label(text="_____", fg="snow", bg="#E6624C")
    labels.append(label)

to_guess = len(chosen_name)

guessed_words = []


# Functions
def get_input():
    global lives
    global to_guess

    entered = entry.get().lower()

    alpha_check = entered.isalpha()

    if not alpha_check:
        messagebox.showwarning(
            "Only Alphabets!!!", f"You entered '{entered}'\nPlease enter only alphabets")
        entry.delete(0, END)
        return

    if entered in guessed_words:
        messagebox.showwarning(
            "Already Guessed", f"You have already guessed the letter '{entered}'\nTry next one.")

    # Deleting the entry
    entry.delete(0, END)

    if len(entered) < 1:
        messagebox.showwarning(
            "Warning", "Please enter a valid character and try again.")
    if len(entered) > 1:
        messagebox.showwarning("Warning", "Please enter only one character.")
    counter = -1
    check = False
    for char in chosen_name:
        counter += 1
        if entered == char and entered not in guessed_words:
            labels[counter].config(text=char.upper(), padx=20)
            to_guess -= 1
            check = True
    if not check and len(entered) == 1 and entered not in guessed_words:
        lives -= 1
        life_indicator.config(text=f"Lives: {lives}", bg="#E6624C")
        messagebox.showwarning(
            "Wrong Guess", f"'{entered}' not in name\nTry again")
    if lives == 0:
        messagebox.showinfo(
            "Game Ends", f"You have lost your lives.\nBetter luck next time!!!\nThe name was {chosen_name}.")
        counter = -1

        for char in chosen_name:
            counter += 1
            labels[counter].config(text=char.upper(), padx=20)
    if to_guess == 0:
        messagebox.showinfo("Congratulations!!!",
                            "You guessed it.\nYou have won!!!\😃")
    guessed_words.append(entered)


y_val = 175
x_val = 25
for i in labels:
    i.place(x=x_val, y=y_val)
    x_val += 65
    i.config(font=("Ubuntu", 15))

# Entry box
entry = Entry(root, width=20, bg="#6EFFC0", borderwidth=3, font=("Bold", 12))
entry.place(x=(x_size / 2) - 55, y=100)
entry.focus_set()

# Enter text label
enter_label = Label(root, text="Enter :", bg="#E6624C",
                    fg="#992714", font=("forte", 20))
enter_label.place(x=x_size / 2 - 150, y=90)

# Submit button
button_img = PhotoImage(file="submit-removebg-preview-removebg-preview.png")
button = Button(root, image=button_img, command=get_input,
                bg="#E6624C", highlightthickness=0, bd=0)
button.place(x=x_size / 2 - 50, y=250)

# Life indicator
life_indicator = Label(
    root, text=f"Lives: {lives}", bg="#E6624C", font=("forte", 25), fg="#4CE6A3")
life_indicator.place(x=x_size - 135, y=0)

root.mainloop()
