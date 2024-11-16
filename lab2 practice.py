#program 1
a = 2 % 2 + 2 * 2 - 2 / 2 ;
print(a)
#program 2
b = 3 / 2 + 5 * 4 / 3 ;
print(b)
#program 3
c = b = a = 3 + 4 ;
print(c)
#program 4
r=eval(input("Enter radius:"))
PI=3.142
area=r**2*PI
print("The area of circle of radius",r,"is:",area)
#program 5
no1=eval(input("Enter first number:"))
no2=eval(input("Enter second number:"))
print("The addition of",no1,"and",no2,"is:",no1+no2)
print("The subtraction of",no1,"and",no2,"is:",no1-no2)
print("The multiplication of",no1,"and",no2,"is:",no1*no2)
print("The division of",no1,"and",no2,"is:",no1/no2)
#program 6
feet,inch=eval(input("Enter height:"))
inches=feet*12+inch
centimeter=inches*2.54
print(feet,"'",inch,"in centimeter are:",centimeter,"cm")
#program 7
x1,x2,y1,y2=eval(input("Enter the 4 points of distance:"))
distance=((x2-x1)**2+(y2-y1)**2)**1/2
print("The total distance is:",distance)
