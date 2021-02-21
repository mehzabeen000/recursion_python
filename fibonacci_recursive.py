# Program to print the fibonacci series upto n_terms 
def fibonacci(n): 
   if n <= 1: 
       return n 
   else: 
       return(fibonacci(n-1) + fibonacci(n-2)) 
n_terms = int(input("Enter the number of terms you want in Fibonacci Series"))
if n_terms>0:
   for i in range(n_terms): 
       print(fibonacci(i)) 


    