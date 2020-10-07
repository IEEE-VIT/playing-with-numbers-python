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
  num=int(input("Enter your number: "))
  f=1
  if(num<0):
    print("Invalid number, Try positive integers")
  elif(num==0):
    pass
  else:
    for i in range(1,num+1):
      f=f*i
  print("Factorial of the number is: ",f)

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
        


if __name__=='__main__':
  add()
  multiply()
  factorial()
  prime()
