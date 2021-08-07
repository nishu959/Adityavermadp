import sys

x = input()
y = input()

a= len(x)
b = len(y)

dp = [[None for i in range(b+1)]for j in range(a+1)]

def lcsubstring(x, y, lx, ly):
  if(lx==0 or ly ==0):
    
    dp[lx][ly] = 0
    return 0
    
  if(dp[lx][ly]!=None):
    return dp[lx][ly]
  
  
  if(x[lx-1]==y[ly-1]):
    
    ans = 1 + lcsubstring(x, y, lx-1, ly-1)
    dp[lx][ly] = ans
    return ans
    
  else:
    
    lcsubstring(x, y, lx, ly-1)
    lcsubstring(x, y, lx-1, ly)
    dp[lx][ly] = 0
    return 0
   
 
lcsubstring(x, y, a, b)


mx = -sys.maxsize 

for i in dp:
  for j in i:
    if(j!=None):
      mx = max(mx, j)
    
print(mx)
    

