#file read and write challenge
# question 1:Create a program that reads a file and writes a modified version to a new file.
with open("input.txt", "r") as file:
    data = file.read()
    modified_data = data.upper()

with open("output.txt", "w") as file:
    data = file.write(f"This is the modified version\n{modified_data}")
    print("file has been successfully created and modified.")

# guestion 2: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
file_1 = input("input file: ")
try:
   with open(file_1, "r") as  file:
       data = file.read()
       print(data)
except FileNotFoundError:
    print("file do not exist")