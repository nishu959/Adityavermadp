n = int(input())
s = input()

import sys

#look constraints 

dp = [[None for i in range(1001)] for j in range(1001)]


def ispalindrom(s, i, j):
  
  if(i==j):
    return True
   
  if(i>j):
    return True
   
  while(i<j):
    
    if(s[i]!=s[j]):
      return False
    i+=1
    j-=1
     
  return True
 


def solve(s, i, j):
  
  if(i>=j):
    return 0
   
  if(ispalindrom(s, i, j)):
    return 0
  
  if(dp[i][j]!=None ):
    return dp[i][j]
  
  #i to j-1
  
  
  mn = sys.maxsize 
  
  for k in range(i, j):
    #1 means one partition done
    
    if(dp[i][k]!=None):
      left = dp[i][k]
      
    else:
      left = solve(s, i, k)
      dp[i][k] =left
     
     
      
    if(dp[k+1][j]!=None):
      right = dp[k+1][j]
      
    else:
      right = solve(s, k+1, j)
      dp[k+1][j] = right
    
    ans = 1 + left + right
    
    mn = min(mn, ans)
    
  
  dp[i][j] = mn
  return mn
  


print(solve(s, 0,n-1)) 

