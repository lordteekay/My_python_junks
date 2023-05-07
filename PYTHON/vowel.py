#Python program to remove vowels from a string
print("The following python program removes vowels from a string");
def remove_vowels(string):
	vowels=('a','e','i','o','u');
	newString=string.lower()
	for x in newString:
		if x in vowels:
			newString=newString.replace(x,'');
	return newString;
string=str(input("Enter a sentence:"));
result=remove_vowels(string);
print("Removing the vowels...");
print("The new sentence without the vowels:"+result);
