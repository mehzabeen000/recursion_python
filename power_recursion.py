#Program to print the power of particular number
def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
num=int(input("Enter the number"))
pow=int(input("Enter the power"))
print(power(num,pow))
