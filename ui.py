from tkinter import *


def send_message():
    print(text_entry.get("1.0", 'end-1c'))
    app.destroy()


# window object
app = Tk()
app.grid_columnconfigure(1, weight=1)

app.title('Admission Form')
app.geometry('540x540')
app.iconbitmap("assets/icon_sdis.ico")

# Message
copied_text = StringVar()
instruction_label = Label(app, text='Paste the text', font=('bold', 14), pady=35)
instruction_label.grid(row=0, column=1, sticky=N)
text_entry = Text(app, width=50, height=20, font=("Bold", 10))
text_entry.grid(row=1, column=1)

# Buttons
generate_btn = Button(app, text='Generate Form', width=12, command=send_message)
generate_btn.grid(row=2, column=1, pady=20)

# Footer
credit_label = Label(app, text='Developed by Alif © Springdale International School- 2022', font=('bold', 10))
credit_label.grid(row=5, column=1, sticky=N)
# start
app.mainloop()
