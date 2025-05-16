def ite(x,n):
    x=1
    while x<=n:
        print(f"hola{x}")
        x += 1
def rec(x,n):
   if x==n:
     print(f"hola{x}")
   else:
       print(f"hola{x}")
       rec(x+1,n)
def ite2(n):
    x=n
    while x>=1:
        print(f"hola{x}")
        x -= 1
def rec2(x):
    if x==1:
        print(f"hola{x}")
    else:
        print(f"hola{x}")
        rec2(x-1)
       
#####
rec2(10)