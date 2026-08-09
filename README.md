# 🔐 PixelGuard - Image Encryption Tool

A Python-based image encryption and decryption application developed using pixel manipulation techniques.

This project was created as part of the **ProDigy InfoTech Cyber Security Internship - Task 02**.

## ✨ Features

- 🖼️ Select PNG, JPG, JPEG and BMP images
- 🔒 Encrypt images using pixel manipulation
- 🔓 Decrypt encrypted images
- 🔑 User-defined encryption key
- ✅ Key validation from 1 to 255
- 📁 Automatic encrypted/decrypted output folders
- 🌓 Dark, Light and System themes
- 🖥️ User-friendly CustomTkinter GUI
- ⚠️ Input validation and error handling

## 🛠️ Technologies Used

- Python
- Pillow
- CustomTkinter
- Tkinter

## 🔐 How It Works

The application manipulates the RGB values of every pixel.

### Encryption

For each RGB channel:

```text
Encrypted Pixel = (Original Pixel + Key) % 256