a = input()
b = input()

dp = {}

def solve(a, b):
 
  if(a==b):
    return True
   
  if(len(a)<=1):
    return False
   
  flag = False
  
  temp = a + b
  
  
  if temp in dp:
    return dp[temp]
  
  
  n = len(a)
  
  for i in range(1,n):
   
    cond1 = solve(a[:i], b[i+1:]) and solve(a[i:], b[:i+1])
   
    cond2 = solve(a[:i], b[:i]) and solve(a[i+1:], b[i+1:])
   
    if(cond1 or cond2):
      flag =  True
      break
      
  dp[temp] = flag
    
  return flag
  
  

if(len(a)!=len(b)):
  print("False")
  
elif(a==""):
  print("True")
else:
  
  print(solve(a, b))
 

