import sys

egg = int(input())

floor = int(input())

dp = [[None for i in range(floor+1)]for j in range(egg+1)]

def solve(e, f):
  
  if(f == 0 or f==1):
    return f
   
  if(e==1):
    return f
  
  
  if(dp[e][f]!=None):
    return dp[e][f]
    
   
  mn = sys.maxsize
  
  for k in range(1,f+1):
    
    if(dp[e-1][k-1]!=None):
      df = dp[e-1][k-1]
    else:
      df = solve(e-1, k-1)
      dp[e-1][k-1] = df
      
      
    if(dp[e][f-k]!=None):
      uf = dp[e][f-k]
    else:
      uf = solve(e, f-k)
      dp[e][f-k] = uf
      
    temp = 1+  max(df, uf)
    
    
    mn = min(temp, mn)
  
  dp[e][f] = mn
  
  return mn
 
 
 
print(solve(egg, floor))

