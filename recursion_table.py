#Program to print the table
def table(n,i=1):
    print(num,"*",i,"=" ,n*i)
    i+=1
    if i<=10:
        table(n,i)
num=int(input("Enter the table number"))
table(num)


