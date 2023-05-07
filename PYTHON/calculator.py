print("The following program is a simple calculator to calculate our basics maths number of two integers");
print("1 for Addition;2 for Subtraction;3 for Multiplcation;4 for Division;5 to exit");
def addition(num1,num2):
	result=float(num1+num2);
	print("Result:"+str(result));
def subtraction(num1,num2):
	result=float(num1-num2);
	print("Result:"+str(result));
def multiplication(num1,num2):
	result=float(num1*num2);
	print("Result:"+str(result));
def division(num1,num2):
	result=float(num1/num2);
	print("Result:"+str(result));
while True:
	choice=int(input("Enter the following choices above:"));
	if(choice>=1 and choice<=4):
		num1=float(input("Enter the first number:"));
		num2=float(input("Enter the second number:"));
		if(choice==1):
			addition(num1,num2);
		elif(choice==2):
			subtraction(num1,num2);
		elif(choice==3):
			multiplication(num1,num2);
		else:
			division(num1,num2);
	elif(choice==5):
		end=str(input("Do you want to end this program? y/n:"))
		if(end=="y"):
			break;
		else:
			continue;
	else:
		print("You enter the wrong choice")
