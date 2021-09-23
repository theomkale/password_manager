from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for x in range(nr_letters)]
    password_numbers = [random.choice(numbers) for x in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for x in range(nr_symbols)]
    password_list = password_symbols + password_letters + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    data = f"{website} | {username} | {password}\n"
    success_message = f"Are you sure you want to save these details?\n" \
                      f"Website:{website}\n" \
                      f"Username:{username}\n" \
                      f"Password:{password}\n"
    fail_message = "Are you high?\n" \
                   "Please add all the fields mentioned."
    if len(password) == 0 and len(username) == 0 and len(website) == 0:
        valid = False
    else:
        valid = True

    if not valid:
        msg = messagebox.showinfo(title=website_label, message=fail_message)
    else:
        msg = messagebox.askyesno(title=website_label, message=success_message)

    if valid:
        with open("secret.txt", mode="a") as file:
            file.write(data)
        if msg:
            messagebox.showinfo(title="Success", message=f"You can forget {password} now ;-)")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx="20", pady="20")

canvas = Canvas(width=200, height=200, )
canvas.grid(row=0, column=1)
image = PhotoImage(file='pass.png')
canvas.create_image(100, 100, image=image)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="E")

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.insert(0, pyperclip.paste())

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="E")

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "theomkale@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
