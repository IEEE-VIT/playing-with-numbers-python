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
        
def perfect_square():
  n = int(input("Enter a number: "))
  x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
    return True

if __name__=='__main__':
  add()
  multiply()
