import sys



n =int(input())

l = list(map(int, input().split()))

#look for constraints to devlare dp array

dp = [[None for i in range(1001)] for j in range(1001)]

def solve(l, i, j):
  mn =  sys.maxsize 
  
  if(i >=j):
    return 0
  
  if(dp[i][j]!=None):
    return dp[i][j] 
  
  for k in range(i, j):
    
    temp = solve(l, i, k) + solve(l, k+1, j) + l[i-1] * l[k] * l[j]      
    
    mn = min(mn, temp)
   
  
  dp[i][j] = mn
  return mn
 
 

print(solve(l, 1, n-1))


