import os
os.chdir('Desktop')
file=open('file.txt','r')
file2=open('file2.txt','w')
for line in file.readlines():
    newLine=line[::-1]
    file2.write(newLine)
    
file.close()
file2.close()

