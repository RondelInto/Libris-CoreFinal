import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk   # You'll need pillow installed: pip install pillow
from db.queries import authenticate_user
from config import COLORS

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Libris Core Login")
        self.root.geometry("400x350")
        self.root.configure(bg=COLORS['background'])

        # Load logo image from assets folder
        logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'libriscore_logo.png')
        try:
            logo_img = Image.open(logo_path)
            logo_img = logo_img.resize((100, 100), Image.ANTIALIAS)
            self.logo_photo = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(root, image=self.logo_photo, bg=COLORS['background'])
            logo_label.pack(pady=(10, 0))
        except Exception as e:
            print(f"Could not load logo image: {e}")

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Label(root, text="Username:", bg=COLORS['background'], fg=COLORS['text_primary'], font=('Arial', 12)).pack(pady=10)
        tk.Entry(root, textvariable=self.username_var, font=('Arial', 12)).pack()

        tk.Label(root, text="Password:", bg=COLORS['background'], fg=COLORS['text_primary'], font=('Arial', 12)).pack(pady=10)
        tk.Entry(root, textvariable=self.password_var, font=('Arial', 12), show="*").pack()

        tk.Button(root, text="Login", bg=COLORS['primary'], fg="white",
                  font=('Arial', 12, 'bold'), command=self.login).pack(pady=20)

    def login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Required", "Please enter both username and password.")
            return

        user = authenticate_user(username, password)
        if user:
            messagebox.showinfo("Success", f"Welcome {user['name']}!")
            self.root.withdraw()  # Hide login window
            # Proceed to user dashboard or admin, etc.
        else:
            messagebox.showerror("Failed", "Invalid username or password.")