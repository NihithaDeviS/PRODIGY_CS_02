from PIL import Image
from pathlib import Path


def validate_key(key):
    """Validate the encryption key."""
    try:
        key = int(key)
    except ValueError:
        raise ValueError("Encryption key must be a number.")

    if not 1 <= key <= 255:
        raise ValueError("Encryption key must be between 1 and 255.")

    return key


def process_image(input_path, output_path, key, mode):
    """
    Encrypt or decrypt an image using pixel manipulation.

    mode:
        'encrypt' -> adds key to RGB values
        'decrypt' -> subtracts key from RGB values
    """

    key = validate_key(key)

    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError("Input image was not found.")

    image = Image.open(input_path).convert("RGB")

    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):

            r, g, b = pixels[x, y]

            if mode == "encrypt":
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

            elif mode == "decrypt":
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

            else:
                raise ValueError(
                    "Mode must be 'encrypt' or 'decrypt'."
                )

            pixels[x, y] = (r, g, b)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    image.save(output_path)

    return str(output_path)


def encrypt_image(input_path, output_path, key):
    """Encrypt an image."""
    return process_image(
        input_path,
        output_path,
        key,
        "encrypt"
    )


def decrypt_image(input_path, output_path, key):
    """Decrypt an image."""
    return process_image(
        input_path,
        output_path,
        key,
        "decrypt"
    )


# Simple command-line test
if __name__ == "__main__":

    print("Pixel Image Encryption Tool")
    print("----------------------------")

    image_path = input("Enter image path: ")
    key = input("Enter encryption key (1-255): ")

    try:
        encrypted_file = encrypt_image(
            image_path,
            "encrypted_images/encrypted_image.png",
            key
        )

        print("\nImage encrypted successfully!")
        print(f"Saved to: {encrypted_file}")

    except Exception as error:
        print(f"\nError: {error}")