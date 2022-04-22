from tkinter import *
from tkinter import messagebox
import json
import pyperclip
from password_generator import password_generator 
import os

WINDOW_BG = "black"
FONT = ("Arial", 16)
FIELD_COLORS = "white"
LABEL_COLOR = "white"
FIELD_FONT_COLOR = "red"

#---------------------------------------------------------------------

filepath = os.path.join(os.path.dirname(__file__), 'data.json')

#----------------------------------------------------------------------

def search_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a website to search")
    else:
        try:
            with open(filepath, mode="r", encoding="utf-8") as old_data:
                password_data = json.load(old_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showinfo(title="Oops", message="Sorry, you have not saved any password before")
        else:
            if website in password_data:
                email = password_data[website]["Email"]
                password = password_data[website]["Password"]
                is_clipboard = messagebox.askokcancel(title=website, message=f"Email: {email}\nPassword: {password}"
                                                                             f"\n\nCan we save it to your clipboard ?")
                if is_clipboard:
                    pyperclip.copy(password)
                    messagebox.showinfo(title="Saved to clipboard", message="The password has been saved to clipboard")
            else:
                messagebox.showinfo(title="Oops", message=f"The password for {website}"
                                                          f"\nhas not been saved")


def database(new_entry):
    try:
        with open(filepath, mode = 'r',encoding='utf-8') as old_entry:
            password_data = json.load(old_entry)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        with open(filepath, mode = 'w',encoding='utf-8') as new_password_entry:
            json.dump(new_entry, new_password_entry, indent=4)
    else:
        password_data.update(new_entry)
        with open(filepath, mode = 'w',encoding='utf-8') as old_password_entry:
            json.dump(password_data, old_password_entry, indent=4)
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def add_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you have not left any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Confirm entries", message=f"These are the details you entered:\n\n" +
                                                                        f"Website: {website}"
                                                                        f"\nEmail: {email}" 
                                                                        f"\nPassword: {password}\n\nDo you want to save them?")
    if is_ok:
        new_entry_in_json = {
                website:
                    {
                        "Email": email,
                        "Password": password
                    }
                            }
        pyperclip.copy(password)
        messagebox.showinfo(title="Saved to clipboard", message="The password has been saved to clipboard")
        database(new_entry_in_json)
        

def get_password():
    password = password_generator()
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(END, password)


window = Tk()
window.title("Password Manager")
window.config(
    padx=20, 
    pady=20, 
    bg=WINDOW_BG
    )

#Website
website_label = Label(
    text="Website", 
    bg=WINDOW_BG, 
    padx=20, 
    font=FONT, 
    fg=LABEL_COLOR
    )
website_label.grid(column=0, row=1, sticky=W)  

website_entry = Entry(
    width=30, 
    bg=FIELD_COLORS, 
    fg=FIELD_FONT_COLOR, 
    font=FONT
    )
website_entry.insert(END, string="")
website_entry.grid(column=1, row=1)
website_entry.focus()  

#Email
email_label = Label(
    text="Email/Username", 
    bg=WINDOW_BG, 
    padx=20, 
    font=FONT, 
    fg=LABEL_COLOR
    )
email_label.grid(column=0, row=2, sticky=W)

email_entry = Entry(
    width=30, 
    bg=FIELD_COLORS, 
    fg=FIELD_FONT_COLOR, 
    font=FONT
    )
email_entry.insert(END, string="")
email_entry.grid(column=1, row=2)
email_entry.insert(0, "example@example.xyz")

#Password
password_label = Label(
    text="Password",
    bg = WINDOW_BG,
    font=FONT,
    padx=20,
    fg = LABEL_COLOR
    )
password_label.grid(column=0, row=3, sticky=W)

password_entry = Entry(
    width=30, 
    bg=FIELD_COLORS, 
    fg=FIELD_FONT_COLOR, 
    font=FONT
    )
password_entry.insert(END, string="")
password_entry.grid(column=1, row=3)

#Buttons
search_button = Button(
    text="Search", 
    padx=95, 
    font=FONT, 
    command=search_password
    )
search_button.grid(column=3, row=1)

generate_button = Button(
    text="Generate Password",
    command=get_password, 
    font=FONT
    )
generate_button.grid(column=3, row=3)

add_button = Button(
    text="Add", 
    width=36, 
    command=add_password, 
    font=FONT
    )
add_button.grid(column=1, row=5, columnspan=2, sticky=W)

window.mainloop()
