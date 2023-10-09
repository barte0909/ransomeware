# import os 

# from cryptography.fernet import Fernet

# files = []

# for file in os.listdir():
#    if file == "test.py" or file == "thekey.key" or file == "testd.py":
#       continue
#    if os.path.isfile(file):
#       files.append(file)

# print(files) 



# passkey = "hanabi"

# user_input = input ("Enter Password")

# with open("thekey.key" , "rb") as thekey:
#    passwordkey = thekey.read()

# if passkey == user_input:
   
#    for file in files:
#       with open(file , "rb") as thefile:
#          contents = thefile.read()
#       contents_decrypted = Fernet(passwordkey).decrypt(contents)
#       with open(file , "wb") as thefile:
#          thefile.write(contents_decrypted)
#    print("Successfull retrive your data")      

# else:
#    print("wrong pass")










# import os
# from cryptography.fernet import Fernet

# # Specify the folder path including the drive letter with backslashes
# folder_path = r'C:\test\picture'

# # Initialize a list to store file names
# files = []

# # List files in the specified folder
# for file in os.listdir(folder_path):
#     if file == "test.py" or file == "thekey.key" or file == "testd.py":
#         continue
#     if os.path.isfile(os.path.join(folder_path, file)):  # Use os.path.join to create the full file path
#         files.append(file)

# print(files)



# # Write the encryption key to a file in the script directory
# key_path = os.path.join(os.path.dirname(__file__), "thekey.key")
# with open(key_path, "rb") as thekey:
#     passkey = thekey.read()

# # Encrypt the files in the specified folder
# for file in files:
#     file_path = os.path.join(folder_path, file)  # Get the full file path
#     with open(file_path, "rb") as thefile:
#         contents = thefile.read()
#     contents_decrypted = Fernet(passkey).decrypt(contents)
#     with open(file_path, "wb") as thefile:
#         thefile.write(contents_decrypted)

