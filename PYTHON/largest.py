#This is a program to find the largest number out of three numbers
print("This code will print the largest three numbers");
def largest(num1,num2,num3):
	largest=num1;
	if(num2>largest):
		largest=num2;
	elif(num3>largest):
		largest=num3;
	else:
		largest=num1
	return largest;
num1=int(input("Enter the first number:"));
num2=int(input("Enter the second number:"));
num3=int(input("Enter the third number:"));
largestNum=largest(num1,num2,num3);
print("The largest number is:"+str(largestNum));
