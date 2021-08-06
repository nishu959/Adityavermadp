import sys

n = int(input())

l = list(map(int, input().split()))

target = sum(l)

dp = [[None for i in range(target+1)] for j in range(n+1)]


#INITIALISATION
for i in range(0,n+1):
  for j in range(0,target+1):
    if(i==0):
      dp[i][j] = False
    
    if(j==0):
      dp[i][j] = True
      
    
   
for i in range(1,n+1):
  for j in range(1,target+1):
    
    if(j >= l[i-1]):
      
      dp[i][j] = dp[i-1][j] or dp[i-1][j-l[i-1]]
      
    else:
      
      dp[i][j] = dp[i-1][j]

p = sys.maxsize 


for i in range(len(dp[n])//2):
  if(dp[n][i]==True):
    
    p = min(p, target- 2*i)
    
 
print(p)
    
  