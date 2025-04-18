file_1 = input("input file:")
try:
   with open(file_1, "r") as  file:
       data = file.read()
       print(data)
except FileNotFoundError:
    print("file do not exist")
    
    

