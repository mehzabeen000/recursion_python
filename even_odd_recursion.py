#Program to print the odd and even number
def number(num=1):
  if num%2==0:
    print(num,"= Even")
  else:
    print(num,"= Odd")
  num+=1
  if num<=100:
    number(num)
number()