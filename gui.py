import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import main

def generate_password_callback():
    global password
    length = 0

    try:
        length = int(password_length_entry.get())
        if length <= 0:
            messagebox.showerror(title = "Invalid Input", message = "Password must be a positive integer.")
    except ValueError:
        messagebox.showerror(title = "Invalid Input", message = "Password must be a positive integer.")

    if not length: return

    char_set = main.generate_char_set(use_lower_var.get(), use_upper_var.get(), use_numbers_var.get(), use_special_var.get())
    generated_password = main.generate_password(length, char_set)
    
    password.set(generated_password)

def copy():
    output_password.clipboard_clear()
    output_password.clipboard_append(password.get())

root = ctk.CTk()

width, height = 640, 640

root.update_idletasks()

x = root.winfo_screenwidth() // 2 - width // 2
y = root.winfo_screenheight() // 2 - height // 2

use_lower_var = ctk.IntVar()
use_upper_var = ctk.IntVar()
use_numbers_var = ctk.IntVar()
use_special_var = ctk.IntVar()
password = ctk.StringVar()

copy_icon = ctk.CTkImage(Image.open("assets/copy-icon.png"))

root.geometry(f"{width}x{height}+{x}+{y}")
root.title("Password generator")

ctk.CTkLabel(root, text = "Password Generator", font = ("Arial", 40)).pack()

input_frame = ctk.CTkFrame(root)

ctk.CTkLabel(input_frame, text = "Password Length: ").pack(side = "left", padx = 10)

password_length_entry = ctk.CTkEntry(input_frame, placeholder_text = "Password Length")
password_length_entry.pack(side = "left", padx = 10)

input_frame.pack(pady = 25)

conditions_frame = ctk.CTkFrame(root)
conditions_frame.pack(pady = 10)

ctk.CTkCheckBox(conditions_frame, text = "Use Lowercase", variable = use_lower_var).pack(side = "left", padx = 10)
ctk.CTkCheckBox(conditions_frame, text = "Use Uppercase", variable = use_upper_var).pack(side = "left", padx = 10)
ctk.CTkCheckBox(conditions_frame, text = "Use Numbers", variable = use_numbers_var).pack(side = "left", padx = 10)
ctk.CTkCheckBox(conditions_frame, text = "Use Special",variable = use_special_var).pack(side = "left", padx = 10)

ctk.CTkButton(root, text = "Generate", command = generate_password_callback).pack(pady = 15)

output_frame = ctk.CTkFrame(root)

ctk.CTkLabel(output_frame, text = "Generated Password: ").pack(side = "left")
output_password = ctk.CTkEntry(output_frame, state = "readonly", textvariable = password, width = 250, height = 50)
output_password.pack(side = "left", padx = 15)
ctk.CTkButton(output_frame, image = copy_icon, text = "", command = copy).pack(side = "left", padx = 10)

output_frame.pack(pady = 10)

root.mainloop()