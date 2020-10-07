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
  a=int(input())
  f=1
  if(a>1):
    for i in range(1,a):
      f=f*i
  return f
def prime():
  # Take an integer n
  # Check whether it is a Prime or not
  # Return true or false

if __name__=='__main__':
  add()
  multiply()
