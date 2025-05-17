#Write a script to calculate the area and perimeter of a rectangle
length = 15
width = 7
area = length*width
perimeter = 2*(length+width)
print(f"the length is :{length} and the width is:{width}")
print(f"area is :{area}")
print(f"Perimeter: {perimeter}")

'''Write a script that takes two numbers as input and prints whether 
the first number is greater than, less than, or equal to the second 
number. 1'''

n1 = float(input("enter the 1st number:"))
n2 = float(input("enter the 2nd number:"))
if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n1 < n2:
    print(f"{n1} is less than {n2}")
else:
    print(f"{n1} is equal to {n2}")

#Leap Year
yr = int(input("Enter the year: "))


if (yr % 400 == 0) or (yr%100 !=0 and yr%4 ==0):
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")

#Concatenate
a= "Gyan"
b= "Deep"
c= a+b
print(c)