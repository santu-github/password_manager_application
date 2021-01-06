from tkinter import *
from tkinter import messagebox
import random
from random import shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, f"{password}")
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_content = website_input.get()
    email_content = email_username_input.get()
    password_content = password_input.get()
    if len(website_content) == 0 or len(password_content) == 0 :
        messagebox.showwarning(title="FIELDS CAN'T BE EMPTY", message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website_content,
                                     message=f"There are the details entered :\nEmail:{email_content}"
                                                               f"\nPassword:{password_content} \n Is it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_content} | {email_content} | {password_content}\n")

            website_input.delete(0, END)

            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.iconbitmap("locker.ico")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website = Label(text="Website: ")
website.grid(column=0, row=1)
website_input = Entry(width=70)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)
email_username = Label(text="Email/Username: ")
email_username.grid(column=0, row=2)
email_username_input = Entry(width=70)
email_username_input.insert(0, "kumarsantos7033@gmail.com")
email_username_input.grid(column=1, row=2, columnspan=2)
password = Label(text="Password: ")
password.grid(column=0, row=3)
password_input = Entry(width=50)
password_input.grid(column=1, row=3)
generate_password = Button(text="Generate Password", width=14, command= generate)
generate_password.grid(column=2, row=3)
add_button = Button(text="Add", width=60, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
