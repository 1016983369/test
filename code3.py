try:
 n=eval(input())
 if isinstance(n,int):
  if "3" or "4" in n:
    print("true")
  else:
    print("false")
except:
    print("illegal input")