def add():
  x = int(input("Enter your number 1: "))
  y = int(input("Enter your number 2: "))
  z = x+y
  print("Your final result is: ", z)

def multiply():
  x = int(input("Enter your number 1: "))
  y = int(input("Enter your number 2: "))
  z = x*y
  print("Your final result is: ", z)

def factorial():
  x = int(input("enter your number:"))
  if x < 0:
   print("Factorial does not exist for negative numbers")
elif x == 0:
   print("The factorial of 0 is 1.")
else:
  factorial=1
   for i in range(1,x + 1):
       factorial = factorial*i
   print("The factorial of",x,"is",factorial)


def prime():
  num = int(input("Enter a number: "))
  if num>1:
    flag=0
    for i in range(2,num):
        if (num % i) == 0:
            flag=0
            break
        else:
            flag=1
    if flag==0:
        print("False")
    else:
        print("True")
  else:
    print("False") 
        
def palindrome():
  n = int(input("Enter a number: "))
  s=0
  t=n
  while t>0:
    r=t%10
    s=s*10+r
    t=t//10
  if n==s:
    print("Palindrome")
  else:
    print("Not Palindrome")

if __name__=='__main__':
  add()
  multiply()
  factorial()
  prime()
  palindrome()

