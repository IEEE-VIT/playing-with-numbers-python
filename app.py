def add():
  x = input("Enter your number 1")
  y = input("Enter your number 2")
  z = x+y
  print("Your final result is: ", z)

def multiply():
  x = input("Enter your number 1")
  y = input("Enter your number 2")
  z = x*y
  print("Your final result is: ", z)

def factorial():
  x = input("enter your number:")
  if x < 0:
   print("Factorial does not exist for negative numbers")
elif x == 0:
   print("The factorial of 0 is 1.")
else:
   for i in range(1,x + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

def prime():
  # Take an integer n
  # Check whether it is a Prime or not
  # Return true or false

if __name__=='__main__':
  add()
  multiply()
