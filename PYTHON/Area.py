import math
print("The following program is used to calculate the area of a circle,The program stops when you enter 0");
def area_of_circle():
	while (True):
		radius=int(input("Enter the radius of the circle:"));
		if(radius==0):
			break;
		else:
			pi=math.pi;
			result=float(pi*(radius**2));
			print("The Area of the circle is:"+str(result));
area_of_circle();
