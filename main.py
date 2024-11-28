from tkinter import *


def save():
    entered_website = website_text.get()
    entered_email= email_text.get()
    entered_password = password_text.get()
    with open("data.txt", mode='a') as data:
        data.write(f"{entered_website} | {entered_email} | {entered_password}\n")
        website_text.delete(0,END)
        email_text.delete(0,END)
        email_text.insert(0,"@gmail.com")
        password_text.delete(0,END)

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file = "logo.png")
canvas.create_image(100,95, image=logo_img)
canvas.grid(row=0, column = 1)

#Website text box and label
website_text = Entry(width = 36)
website_text.grid(row=1,column=1,columnspan = 2, sticky=EW)
website_text.focus()
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky=EW)

#email text box and label
email_text = Entry(width = 36)
email_text.grid(row=2,column=1, columnspan = 2, sticky=EW)
email_text.insert(index=0,string="@gmail.com")
email_label = Label(text = "Email/Username:")
email_label.grid(row=2,column=0, sticky=EW)

#generate button and password text entry
password_text = Entry(width=21)
password_text.grid(row=3,column=1, sticky=EW)
generate_button = Button(text = "Generate",width= 9)
generate_button.grid(column = 2, row=3, sticky=EW)
password_label = Label(text = "Password: ")
password_label.grid(row=3, column = 0, sticky=EW)

#add button
add_button = Button(text = "Add",width=36,command = save)
add_button.grid(row=4, column = 1,columnspan = 2, sticky=EW)



window.mainloop()
