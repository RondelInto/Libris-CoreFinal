# ui/user_dashboard.py
import tkinter as tk
from config import COLORS

class UserDashboard:
    def __init__(self, root, user):
        self.root = root
        self.root.title(f"Libris Core - User Dashboard ({user['name']})")
        self.root.geometry("800x600")
        self.root.configure(bg=COLORS['background'])
        self.user = user

        header = tk.Frame(root, bg=COLORS['primary'], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        tk.Label(header, text=f"Welcome, {user['name']} (User)", bg=COLORS['primary'], fg='white', font=('Arial', 16, 'bold')).pack(side=tk.LEFT, padx=20, pady=15)

        logout_btn = tk.Button(header, text="Logout", bg=COLORS['primary_light'], fg='white', relief=tk.FLAT, command=self.logout, padx=10)
        logout_btn.pack(side=tk.RIGHT, padx=20, pady=15)

        body = tk.Frame(root, bg=COLORS['background'])
        body.pack(expand=True, fill=tk.BOTH)

        tk.Label(body, text="This is a basic user dashboard.\nExpand this with features like browse/search books, borrowing, and profile.",
                 bg=COLORS['background'], fg=COLORS['text_secondary'], font=('Arial', 12), justify=tk.LEFT).pack(padx=20, pady=20, anchor='w')

    def logout(self):
        self.root.destroy()
        # Optionally, show login window again if needed