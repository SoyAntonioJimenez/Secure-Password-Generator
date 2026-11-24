import tkinter as tk
from tkinter import ttk, messagebox
import string
import secrets

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Secure Password Generator")

        # Color configuration
        background_color = "#121212"  # Background color set to a darker shade
        text_color = "#FFA500"       # Dark orange text color
        accent_color = "#3498db"     # Accent color

        # Window configuration
        self.configure(bg=background_color)

        # Style configuration
        style = ttk.Style(self)
        style.configure("TLabel", foreground=text_color, background=background_color, font=("Helvetica", 12))
        style.configure("TButton", foreground=background_color, background=accent_color, borderwidth=0, font=("Roboto", 12, "bold"))
        style.map("TButton", foreground=[('pressed', 'black'), ('active', 'black')], background=[('pressed', accent_color), ('active', accent_color)])
        style.configure("TCheckbutton", background=background_color, foreground=text_color, font=("Helvetica", 12))
        style.configure("TEntry", foreground=background_color, insertbackground=background_color, font=("Roboto", 12, "bold"))
        style.configure("TEntry.Length", foreground="#333333", insertbackground="#333333", font=("Helvetica", 12))
        style.configure("TText", foreground=text_color, insertbackground=text_color, font=("Helvetica", 12))

        # Interface elements
        self.label_length = ttk.Label(self, text="Length:", style="TLabel")
        self.label_length.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.length_var = tk.IntVar()
        self.length_var.set(20)
        self.entry_length = ttk.Entry(self, textvariable=self.length_var, style="TEntry")
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)

        self.checkbox_numbers_var = tk.BooleanVar()
        self.checkbox_numbers = ttk.Checkbutton(self, text="Include numbers", variable=self.checkbox_numbers_var, style="TCheckbutton")
        self.checkbox_numbers.grid(row=1, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        self.checkbox_symbols_var = tk.BooleanVar()
        self.checkbox_symbols = ttk.Checkbutton(self, text="Include symbols", variable=self.checkbox_symbols_var, style="TCheckbutton")
        self.checkbox_symbols.grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        self.checkbox_asian_characters_var = tk.BooleanVar()
        self.checkbox_asian_characters = ttk.Checkbutton(self, text="Include Asian characters", variable=self.checkbox_asian_characters_var, style="TCheckbutton")
        self.checkbox_asian_characters.grid(row=3, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        self.checkbox_arabic_characters_var = tk.BooleanVar()
        self.checkbox_arabic_characters = ttk.Checkbutton(self, text="Include Arabic characters", variable=self.checkbox_arabic_characters_var, style="TCheckbutton")
        self.checkbox_arabic_characters.grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        self.checkbox_other_characters_var = tk.BooleanVar()
        self.checkbox_other_characters = ttk.Checkbutton(self, text="Include other characters", variable=self.checkbox_other_characters_var, style="TCheckbutton")
        self.checkbox_other_characters.grid(row=5, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        self.checkbox_unicode_var = tk.BooleanVar()
        self.checkbox_unicode = ttk.Checkbutton(self, text="Include Unicode characters", variable=self.checkbox_unicode_var, style="TCheckbutton")
        self.checkbox_unicode.grid(row=6, column=0, columnspan=2, padx=20, pady=5, sticky="w")

        self.button_generate = ttk.Button(self, text="✔ Generate Password", command=self.generate_password, style="TButton")
        self.button_generate.grid(row=7, column=0, columnspan=2, pady=10)

        self.text_password = tk.Text(self, height=4, width=40, wrap=tk.WORD, bg=background_color, fg=text_color, insertbackground=text_color, font=("Helvetica", 12))
        self.text_password.grid(row=8, column=0, columnspan=2, padx=20, pady=10)

        # Enable the copy option in the context menu for both left and right clicks
        self.text_password.bind("<Button-1>", self.show_context_menu)
        self.text_password.bind("<Button-3>", self.show_context_menu)

        # Disable direct text selection in the Text widget
        self.text_password.bind("<B1-Motion>", lambda event: "break")  # Disable drag to select
        self.text_password.bind("<B2-Motion>", lambda event: "break")  # Disable middle-click paste
        self.text_password.bind("<B3-Motion>", lambda event: "break")  # Disable right-click context menu selection

    def generate_password(self):
        length = self.length_var.get()

        characters = string.ascii_letters
        if self.checkbox_numbers_var.get():
            characters += string.digits
        if self.checkbox_symbols_var.get():
            characters += string.punctuation
        if self.checkbox_asian_characters_var.get():
            # Examples of Asian characters (Chinese, Japanese, Korean, Thai)
            characters += "你好世界こんにちは안녕하세요สวัสดี"
            characters += "您好世界さようなら안녕하세요สวัสดี"
        if self.checkbox_arabic_characters_var.get():
            # Examples of Arabic characters
            characters += "مرحبا بكم"
            characters += "صباح الخير"
            characters += "مساء الخير"
            characters += "السلام عليكم"
            characters += "وداعا"

        if self.checkbox_other_characters_var.get():
            # Examples of other special characters
            characters += "ñáéíóú"
            characters += "ßäöü"
            characters += "æøå"

        if self.checkbox_unicode_var.get():
            # Examples of Unicode characters
            characters += "♔♕♖♗♘♙"
            characters += "♪♫♬"
            characters += "♥♦♣♠"
            characters += "■□▢"
            characters += "→←↑↓"
            characters += "∞∑√"

        generated_password = ''.join(secrets.choice(characters) for _ in range(length))
        self.text_password.delete(1.0, tk.END)  # Clear previous password
        self.text_password.insert(tk.END, generated_password)

    def copy_to_clipboard(self):
        password = self.text_password.get(1.0, tk.END).strip()
        self.clipboard_clear()
        self.clipboard_append(password)
        self.update()

    def show_context_menu(self, event):
        context_menu = tk.Menu(self, tearoff=0)
        context_menu.add_command(label="Copy", command=self.copy_to_clipboard)
        context_menu.post(event.x_root, event.y_root)

if __name__ == "__main__":
    app = PasswordGenerator()
    app.geometry("400x600")
    app.resizable(0, 0)
    app.mainloop()
