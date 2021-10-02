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

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)

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
    print("Error")

def print_factors():
   x = int(input("Enter a number: "))  
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
        
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

def armstrong():
  n = int(input("Enter a number"))  
  order = len(str(n))
  sum = 0
  temp = n
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
  if n == sum:
    print(n,"is an Armstrong number")
  else:
    print(n,"is not an Armstrong number")

if __name__=='__main__':
  add()
  multiply()
  factorial()
  prime()
  print_factors()
  palindrome()
  

