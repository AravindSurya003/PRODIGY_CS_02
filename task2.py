from PIL import Image
import numpy as np
import pillow as PIL

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixel_array = np.array(image)

    # Create a key array from the key
    key_array = np.frombuffer(key.encode(), dtype=np.uint8)

    # Encrypt the image by performing an XOR operation with the key
    encrypted_pixel_array = pixel_array ^ key_array[:, None, None]

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_pixel_array)
    encrypted_image.save(output_path)

def decrypt_image(encrypted_image_path, output_path, key):
    # The decryption process is the same as encryption because XOR is a reversible operation
    encrypt_image(encrypted_image_path, output_path, key)

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice, please try again.")
            continue
        
        image_path = input("Enter the path to the image file: ")
        output_path = input("Enter the path for the output file: ")
        key = input("Enter the encryption/decryption key: ")

        if choice == 'e':
            encrypt_image(image_path, output_path, key)
            print(f"Encrypted image saved to {output_path}")
        elif choice == 'd':
            decrypt_image(image_path, output_path, key)
            print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    main()
