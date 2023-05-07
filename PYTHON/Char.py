import random
print("This a gambling program,whereby you guess a number between 1 and 5,if the number is what the computer picks,you'll get x20 of your initial deposit")

def gamble():
	guess=int(input("Guess a number:"));
	cheat=random.randint(1,5);
	if (guess == cheat):
		return "Congratulations you won"
	else:
		return "Sorry you lost"
result=gamble();
print(result)

