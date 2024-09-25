a=int(input("Enter the 1st number :"))
b=int(input("Enter the 2nd number :"))
c=int(input("Enter the 3rd number :"))
if(a>b & a>c):
    print("The Greatest number is :",a)
elif(b>a & b>c):
    print("The greatest Number is :",b)
else:
    print("The greatest Number is ",c)