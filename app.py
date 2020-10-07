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
  # Take an integer as an input and
  # Return it's factorial 

def prime():
  x = input("Enter a number:")
  fac = 1
  if x<0:
    print("factorial not possible")
  elif x==0:
    print("factorial is 1)
  else:
    for i in range(1,num + 1):
          fac = fac * i
    print("factorial is:",fac)
if __name__=='__main__':
  add()
  multiply()
  factorial()
