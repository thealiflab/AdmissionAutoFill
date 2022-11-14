from tkinter import *
from tkinter import messagebox


class AppUI:
    def __init__(self):

        # window object
        self.app = Tk()
        self.app.grid_columnconfigure(1, weight=1)

        self.MAIL_TEXT = ""
        self.app.title('Admission Form')
        self.app.geometry('540x540')
        self.app.iconbitmap("assets/icon_sdis.ico")

        # Message
        self.instruction_label = Label(self.app, text='Paste the text', font=('bold', 14), pady=35)
        self.instruction_label.grid(row=0, column=1, sticky=N)
        self.text_entry = Text(self.app, width=50, height=20, font=("Bold", 10))
        self.text_entry.grid(row=1, column=1)

        def send_message():
            self.MAIL_TEXT = self.text_entry.get("1.0", 'end-1c')

            print(self.MAIL_TEXT)

            if len(self.MAIL_TEXT) == 0:
                messagebox.showerror("error", "Text field empty!")
                exit()
            elif len(self.MAIL_TEXT) <= 118:
                messagebox.showerror("error", "Not enough entry text!")
                exit()
            else:
                messagebox.showinfo(title="Success", message="Form has been generated successfully!", )
                self.app.destroy()

        # Buttons
        self.generate_btn = Button(self.app, text='Generate Form', width=12, height=2, command=send_message)
        self.generate_btn.grid(row=2, column=1, pady=20)

        # Footer
        credit_label = Label(self.app, text='Developed by Alif © Springdale International School-2022',
                             font=('bold', 8),
                             pady=15)
        credit_label.grid(row=5, column=1, sticky=N)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                exit()

        self.app.protocol("WM_DELETE_WINDOW", on_closing)

        # start
        self.app.mainloop()
