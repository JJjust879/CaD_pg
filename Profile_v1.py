import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ProfileWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Profile")
        self.configure(bg='light blue')
        self.geometry("800x600")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.create_widgets()
    
    def create_widgets(self):
        # Profile Picture Section
        self.profile_pic_label = tk.Label(self, text="Profile Picture", bg='light blue')
        self.profile_pic_label.grid(row=0, column=1, pady=(10, 0))
        
        self.upload_btn = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_btn.grid(row=1, column=1, pady=(0, 10))

        # User Information Fields
        self.fields = {
            'Username': tk.Entry(self),
            'Password': tk.Entry(self, show='*'),
            'Email': tk.Entry(self),
            'Home Address': tk.Entry(self),
            'Contact Number': tk.Entry(self),
            'Emergency Number': tk.Entry(self),
        }
        
        for idx, (label_text, entry) in enumerate(self.fields.items()):
            label = tk.Label(self, text=label_text, font='Helvetica 10 bold', bg='light blue')
            label.grid(row=2+idx, column=0, padx=10, pady=5, sticky='e')
            entry.grid(row=2+idx, column=1, padx=10, pady=5, sticky='ew')
        
        self.save_btn = tk.Button(self, text="Save", command=self.save_profile)
        self.save_btn.grid(row=8, column=1, pady=20)

        self.logout_btn = tk.Button(self, text="Logout", command=self.logout)
        self.logout_btn.grid(row=0, column=2, pady=10, padx=10, sticky='ne')
        
        self.create_sidebar()

    def create_sidebar(self):
        sidebar = tk.Frame(self, bg='#FFCCCC')
        sidebar.grid(row=9, column=0, columnspan=3, sticky='ew')

        self.grid_rowconfigure(9, weight=1)
        
        buttons = ["Map", "Payment", "Appointment", "Health Record"]
        for idx, btn_text in enumerate(buttons):
            btn = tk.Button(sidebar, text=btn_text, command=lambda bt=btn_text: self.tab_action(bt))
            btn.grid(row=0, column=idx, padx=10, pady=10, sticky='ew')
            sidebar.grid_columnconfigure(idx, weight=1)

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
            self.profile_pic_label.configure(image=image)
            self.profile_pic_label.image = image
    
    def save_profile(self):
        profile_data = {label: entry.get() for label, entry in self.fields.items()}
        messagebox.showinfo("Profile Saved", "Profile information has been saved successfully!")

    def logout(self):
        self.destroy()

    def tab_action(self, tab_name):
        messagebox.showinfo(tab_name, f"You clicked on the {tab_name} tab")

if __name__ == "__main__":
    app = ProfileWindow()
    app.mainloop()
