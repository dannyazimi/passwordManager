from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def save():
    entered_website = website_text.get().title()
    entered_email= email_text.get()
    entered_password = password_text.get()
    new_data = {
        entered_website: {
            "email": entered_email,
            "password": entered_password,
        }
    }

    if len(entered_website) == 0 or len(entered_password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure all the entries are filled.")
    else:
        try:
            with open("data.json", mode='r') as data_file:
                #Read the old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json",mode="w") as data_file:
                json.dump(new_data,data_file, indent = 4)
        else:
            #Update the old data with the new data
            data.update(new_data)

            with open("data.json", mode = "w") as data_file:
                #Saving the updated data back to file
                json.dump(data,data_file, indent=4)
        finally:
            website_text.delete(0,END)
            email_text.delete(0,END)
            email_text.insert(0,"@gmail.com")
            password_text.delete(0,END)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_text.delete(0,END)
    password_text.insert(0,password)
    pyperclip.copy(password)

def website_search():
    search_var = website_text.get().title()

    with open("data.json", mode="r") as data_file:
        data = json.load(data_file)
        search_result = data[search_var]
        print(search_result)
        searched_email = search_result["email"]
        searched_password = search_result["password"]
        messagebox.showinfo(search_var, f"Username: {searched_email}\n Password: {searched_password}\n\n"
                                        f" Password copied to clipboard")
        pyperclip.copy(searched_password)

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,95, image=logo_img)
canvas.grid(row=0, column = 1)

#Website text box and label
website_text = Entry(width = 36)
website_text.grid(row=1,column=1, sticky=EW)
website_text.focus()
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky=EW)
search_button = Button(text="Search",command=website_search,width=20)
search_button.grid(row=1, column=2, sticky=EW)

#email text box and label
email_text = Entry(width = 36)
email_text.grid(row=2,column=1, columnspan = 2, sticky=EW)
email_text.insert(index=0,string="@gmail.com")
email_label = Label(text = "Email/Username:")
email_label.grid(row=2,column=0, sticky=EW)

#generate button and password text entry
password_text = Entry(width=21)
password_text.grid(row=3,column=1, sticky=EW)
generate_button = Button(text = "Generate",width= 9,command=generate_password)
generate_button.grid(column = 2, row=3, sticky=EW)
password_label = Label(text = "Password: ")
password_label.grid(row=3, column = 0, sticky=EW)

#add button
add_button = Button(text = "Add",width=36,command = save)
add_button.grid(row=4, column = 1,columnspan = 2, sticky=EW)



window.mainloop()
