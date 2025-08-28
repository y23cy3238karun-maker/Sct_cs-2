from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    arr = np.array(img)

    # Apply encryption: XOR each pixel value with the key
    encrypted_arr = arr ^ key  

    # Save encrypted image
    encrypted_img = Image.fromarray(encrypted_arr.astype('uint8'))
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted and saved as encrypted_image.png")

def decrypt_image(image_path, key):
    # Open encrypted image
    img = Image.open(image_path)
    arr = np.array(img)

    # Apply decryption (same as encryption since XOR is reversible)
    decrypted_arr = arr ^ key  

    # Save decrypted image
    decrypted_img = Image.fromarray(decrypted_arr.astype('uint8'))
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted and saved as decrypted_image.png")

# Example usage
if __name__ == "__main__":
    key = 123  # simple key
    encrypt_image("input_image.png", key)   # encrypt original image
    decrypt_image("encrypted_image.png", key)  # decrypt back to original