import customtkinter as ctk
from tkinter import filedialog, messagebox
from pathlib import Path

from image_encryptor import encrypt_image, decrypt_image


# -----------------------------
# App Configuration
# -----------------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.title("PixelGuard - Image Encryption Tool")
app.geometry("850x650")
app.resizable(False, False)


# -----------------------------
# Variables
# -----------------------------

selected_image = ""
key_var = ctk.StringVar()


# -----------------------------
# Functions
# -----------------------------

def select_image():
    """Open file dialog and select an image."""

    global selected_image

    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.png *.jpg *.jpeg *.bmp"),
            ("PNG Files", "*.png"),
            ("JPEG Files", "*.jpg *.jpeg"),
            ("All Files", "*.*")
        ]
    )

    if file_path:
        selected_image = file_path

        file_name_label.configure(
            text=f"Selected: {Path(file_path).name}"
        )

        status_label.configure(
            text="Image selected successfully.",
            text_color="green"
        )


def get_key():
    """Read and validate the encryption key."""

    key = key_var.get().strip()

    if not key:
        messagebox.showwarning(
            "Missing Key",
            "Please enter an encryption key."
        )
        return None

    try:
        key = int(key)
    except ValueError:
        messagebox.showerror(
            "Invalid Key",
            "Encryption key must be a number."
        )
        return None

    if key < 1 or key > 255:
        messagebox.showerror(
            "Invalid Key",
            "Encryption key must be between 1 and 255."
        )
        return None

    return key


def encrypt():
    """Encrypt the selected image."""

    if not selected_image:
        messagebox.showwarning(
            "No Image",
            "Please select an image first."
        )
        return

    key = get_key()

    if key is None:
        return

    try:
        input_path = Path(selected_image)

        output_path = (
            Path("encrypted_images")
            / f"{input_path.stem}_encrypted.png"
        )

        encrypt_image(
            selected_image,
            output_path,
            key
        )

        status_label.configure(
            text=f"Encrypted image saved: {output_path}",
            text_color="green"
        )

        messagebox.showinfo(
            "Encryption Complete",
            f"Image encrypted successfully!\n\n"
            f"Saved to:\n{output_path}"
        )

    except Exception as error:

        status_label.configure(
            text="Encryption failed.",
            text_color="red"
        )

        messagebox.showerror(
            "Encryption Error",
            str(error)
        )


def decrypt():
    """Decrypt the selected encrypted image."""

    if not selected_image:
        messagebox.showwarning(
            "No Image",
            "Please select an encrypted image first."
        )
        return

    key = get_key()

    if key is None:
        return

    try:
        input_path = Path(selected_image)

        output_path = (
            Path("decrypted_images")
            / f"{input_path.stem}_decrypted.png"
        )

        decrypt_image(
            selected_image,
            output_path,
            key
        )

        status_label.configure(
            text=f"Decrypted image saved: {output_path}",
            text_color="green"
        )

        messagebox.showinfo(
            "Decryption Complete",
            f"Image decrypted successfully!\n\n"
            f"Saved to:\n{output_path}"
        )

    except Exception as error:

        status_label.configure(
            text="Decryption failed.",
            text_color="red"
        )

        messagebox.showerror(
            "Decryption Error",
            str(error)
        )


def clear():
    """Reset the application."""

    global selected_image

    selected_image = ""

    key_var.set("")

    file_name_label.configure(
        text="No image selected"
    )

    status_label.configure(
        text="Ready",
        text_color="gray"
    )


def change_theme(choice):
    """Change application appearance."""

    ctk.set_appearance_mode(choice)


# -----------------------------
# Header
# -----------------------------

title_label = ctk.CTkLabel(
    app,
    text="🔐 PixelGuard",
    font=("Arial", 34, "bold")
)

title_label.pack(pady=(30, 5))


subtitle_label = ctk.CTkLabel(
    app,
    text="Pixel Manipulation for Image Encryption",
    font=("Arial", 16),
    text_color="gray"
)

subtitle_label.pack(pady=(0, 25))


# -----------------------------
# Main Card
# -----------------------------

main_frame = ctk.CTkFrame(
    app,
    width=700,
    height=390,
    corner_radius=15
)

main_frame.pack(
    padx=50,
    pady=10,
    fill="x"
)

main_frame.pack_propagate(False)


# -----------------------------
# Select Image
# -----------------------------

select_button = ctk.CTkButton(
    main_frame,
    text="📁 Select Image",
    width=220,
    height=45,
    font=("Arial", 15, "bold"),
    command=select_image
)

select_button.pack(pady=(30, 10))


file_name_label = ctk.CTkLabel(
    main_frame,
    text="No image selected",
    font=("Arial", 14),
    text_color="gray"
)

file_name_label.pack(pady=5)


# -----------------------------
# Encryption Key
# -----------------------------

key_label = ctk.CTkLabel(
    main_frame,
    text="Encryption Key (1 - 255)",
    font=("Arial", 16, "bold")
)

key_label.pack(pady=(25, 8))


key_entry = ctk.CTkEntry(
    main_frame,
    width=250,
    height=40,
    textvariable=key_var,
    placeholder_text="Enter a number from 1 to 255"
)

key_entry.pack()


# -----------------------------
# Action Buttons
# -----------------------------

button_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

button_frame.pack(pady=25)


encrypt_button = ctk.CTkButton(
    button_frame,
    text="🔒 Encrypt",
    width=150,
    height=45,
    font=("Arial", 15, "bold"),
    command=encrypt
)

encrypt_button.grid(
    row=0,
    column=0,
    padx=10
)


decrypt_button = ctk.CTkButton(
    button_frame,
    text="🔓 Decrypt",
    width=150,
    height=45,
    font=("Arial", 15, "bold"),
    command=decrypt
)

decrypt_button.grid(
    row=0,
    column=1,
    padx=10
)


clear_button = ctk.CTkButton(
    button_frame,
    text="↻ Clear",
    width=120,
    height=45,
    command=clear
)

clear_button.grid(
    row=0,
    column=2,
    padx=10
)


# -----------------------------
# Status
# -----------------------------

status_label = ctk.CTkLabel(
    app,
    text="Ready",
    font=("Arial", 14),
    text_color="gray"
)

status_label.pack(pady=15)


# -----------------------------
# Theme Selector
# -----------------------------

theme_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

theme_frame.pack(pady=5)


theme_label = ctk.CTkLabel(
    theme_frame,
    text="Theme:",
    font=("Arial", 13)
)

theme_label.pack(
    side="left",
    padx=8
)


theme_menu = ctk.CTkOptionMenu(
    theme_frame,
    values=["Dark", "Light", "System"],
    command=change_theme
)

theme_menu.pack(
    side="left"
)

theme_menu.set("Dark")


# -----------------------------
# Footer
# -----------------------------

footer_label = ctk.CTkLabel(
    app,
    text="ProDigy InfoTech • Cyber Security Internship • Task-02",
    font=("Arial", 11),
    text_color="gray"
)

footer_label.pack(
    side="bottom",
    pady=12
)


# -----------------------------
# Start Application
# -----------------------------

app.mainloop()