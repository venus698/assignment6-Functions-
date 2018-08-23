#Question 1
def Area():
    radius=float(input("Enter the radius of sphere:"))
    area=(4*3.14*(radius**2))
    return area
print("Area of sphere is:",Area())

#Question 2
def perfect(num):
    a=0
    for i in range(1,num):
        if(num%i==0):
            a=a+i
    if(a==num):
        print(num)
for i in range(1,1001):
    perfect(i)
    
#Question 3
a=int(input("Enter number:"))
def table(a):
    for i in range(1,11):
        print("{}*{}=".format(a,i),(a*i))
table(a)

#Question 4
a=int(input("Enter a:"))
b=int(input("Enter b:"))

def fun(b):
    
    if(b==0):
        return 1
    else:
        return a*fun(b-1)
    
print(fun(b))
    

