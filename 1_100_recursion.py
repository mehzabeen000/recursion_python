#Program to print the number from 1 to 100 reverse
def number(num=1):
  print( num)
  num+=1
  if num<=100:
    number(num)
number()

#Program to print the number from 1 to 100
def number(num=100):
  print( num)
  num-=1
  if num>0:
    number(num)
number()

