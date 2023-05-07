import random
guess=random.randint(1,100);
print("I'm thinking of a number between 1 and 100,guess the number");

def guess_number():
	global num;
	for i in range(1,6):
		num=int(input("Enter the number:"));
		if (num>guess):
			print("The number is too high");
		elif (num<guess):
			print("The number is too low");
		
		else:
			break;

def check(arg1,arg2):
	if(arg1==arg2):
		print("Congratulations you guessed the number right");
	else:
		print("Sorry the number is "+str(arg2));
guess_number();
check(num,guess);
