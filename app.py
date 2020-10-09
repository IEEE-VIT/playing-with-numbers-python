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
    
def checkPallindrome():
  num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")
    
def checkArmstrong():
 num = int(input("Enter a number: "))  
sum = 0  
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** 3  
   temp //= 10  
  
if num == sum:  
   print(num,"is an Armstrong number")  
else:  
   print(num,"is not an Armstrong number")  
    
def print_factors():
   num = int(input("Enter a number: "))  
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
        


if __name__=='__main__':
  add()
  multiply()
  factorial()
  prime()
  checkPallindrome()
  checkArmstrong()
  print_factors()
