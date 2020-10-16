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
 num = int(input("Enter a number: "))
  if num>1:
    for i in range(2,num-1):
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
  palindrome()