'''
1. create folder > file.txt > text  
2. pattern 

example: 
*
**
***
****
*****
****
***
**
*

'''

import os 

def createFolder (base_path, folderName, fileName, index):
    if not os.path.exists("data"):
        os.mkdir("data")
    path_name = f"{base_path}\\{folderName}_{index}"
    text = fileName * index
    os.mkdir(path_name)
    with open(f"{path_name}\\{fileName}.txt", 'w') as file:
        file.write(f"{text}")
     
def getFolder(str, base_path):
    for i in range(len(str)):
        folderName = str[i]
        fileName = str[i].lower()
        index = i + 1
        createFolder(base_path, folderName, fileName, index)
    print("\n****Folder created successfully!!!****\n")


DNA_str = "ATGCATCATGC"
base_path  = 'data'

getFolder(DNA_str, base_path)


n = int(input("Enter the number which you want to print: "))

def getPattern(n):
    for i in range(1, n+1):
        print("*" * i) 
    for i in range(n - 1, 0, -1):
        print("*" * i)



getPattern(n)

