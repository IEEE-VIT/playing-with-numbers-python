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
        
        
# a function to replace space with _
def fullname():
  name = input("Enter your fullname: ")
  name = name.replace(" ","_")
  print(name)


if __name__=='__main__':
  add()
  multiply()
  fullname()
