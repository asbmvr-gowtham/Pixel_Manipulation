Pixel Cipher 🔐🖼️
A simple tool to encrypt and decrypt images using pixel scrambling based on a secret key.

📦 1. Install Dependencies
Install the required Pillow library using pip:

bash
Copy
Edit
pip install Pillow
▶️ 2. Run the Script
Execute the script from your terminal:

bash
Copy
Edit
python pixel_cipher.py
(Assuming your Python file is named pixel_cipher.py)

🔒 Encrypting an Image
bash
Copy
Edit
$ python pixel_cipher.py
Select an operation to perform:
1. Encrypt Image
2. Decrypt Image
Enter your choice (1 or 2): 1
Enter the path for the input image: my_photo.png
Enter the path for the output image: encrypted_photo.png
Enter the secret integer key: 12345
Processing 'my_photo.png' with pixel scramble...
Successfully saved to 'encrypted_photo.png'
🔓 Decrypting an Image
To decrypt, run the script again, choose option 2, and use the exact same key.

bash
Copy
Edit
$ python pixel_cipher.py
Select an operation to perform:
1. Encrypt Image
2. Decrypt Image
Enter your choice (1 or 2): 2
Enter the path for the input image: encrypted_photo.png
Enter the path for the output image: original_photo_restored.png
Enter the secret integer key: 12345
Processing 'encrypted_photo.png' with pixel scramble...
Successfully saved to 'original_photo_restored.png'
✅ Notes
The encryption relies on a secret integer key to scramble the pixels.

You must use the same key for both encryption and decryption.

Make sure the input image exists and is in a supported format (e.g., PNG, JPG).
