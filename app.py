def add():
  x = input("Enter your number 1")
  y = input("Enter your number 2")
  z = x+y
  print("Your final result is: ", z)

def multiply():
    x = input("Enter your number 1")
    y = input("Enter your number 2") # Ask the user for the number of values' sum they would like to calculate
    w = x*y # Now, ask each of the number one by one
    print("The value is :",w)# Return the multiplication of all the numbers upto 2 decimal places

def factorial():
  n = input("Enter your number")# Take an integer as an input and
  fact = 1
  for i in range(1,n+1): 
    fact = fact * i 
print (fact)# Return it's factorial 

def prime():
     n = input("Enter your number")# Take an integer n
     if (num % i) == 0: 
        print("false")
     else:
        print("true")# Check whether it is a Prime or not
  # Return true or false

if __name__=='__main__':
  add()
