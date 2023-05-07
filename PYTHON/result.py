#This is a python program to check for exam score for a particular student
print("Hello welcome to class jss3 portal");
print("Note:Only your biology test score has been updated");
students={'moshood':34,'abraham':15,'lekan':12,'ayomide':16,'precious':21,'faith':13,'bolu':32,'gift':8}
name=str(input("Enter your name:"));
subject=str(input("Enter your subject:"));
reName=name.lower();
subject=subject.lower();
if (reName in students and subject=='biology'):
	print("Welcome to your portal "+str(reName));
	print("Loading...");
	print("Your "+str(subject)+" test score is:"+str(students[reName])+"/40");
elif (reName in students and subject!='biology'):
	print("Welcome to your portal "+str(reName));
	print("Your "+str(subject)+" hasn't been uploaded");
else:
	print("Your name is not included to those in jss3,kindly report to your class teacher")
