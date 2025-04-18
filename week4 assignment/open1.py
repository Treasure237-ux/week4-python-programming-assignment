#file read and write challenge
with open("input1.txt", "r") as file:
    data = file.read()
    modified_data = data.upper()
   # print (modified_data)

with open("output1.txt", "w") as file:
    data = file.write(f"This is the modified version\n{modified_data}")
    print("file has been successfully created and modified.")