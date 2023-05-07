print("Password checker");
password=str(input("Enter your password:"));
reTypePassword=str(input("Enter your password again:"));
if(password==reTypePassword):
	print("Loading...");
	print("Correct password!");
else:
	print("Incorrect password,try again");


