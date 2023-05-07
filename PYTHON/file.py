import os
#This is a python program to write to a new created file in our desired directory.
directory=str(input("Enter the directory name:"));
os.chdir(directory);
fileName=str(input("Create a .txt file name:"));
file=open(fileName,'wt');
context=str(input("Enter what you want to put in the file:"));
file.write(context);
file.close();
