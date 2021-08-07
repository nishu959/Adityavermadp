n = int(input())

coin = list(map(int, input().split()))

target = int(input())

dp = [[None for i in range(target+1)] for j in range(n+1)]


for i in range(n+1):
  for j in range(target +1):
    
    if(i==0):
      dp[i][j] = 0
     
    if(j==0):
      dp[i][j] = 1
     
    
for i in range(1,n+1):
  for j in range(1,target +1):
    
    if(j >= coin[i-1]):
      dp[i][j] = dp[i][j-coin[i-1]] + dp[i-1][j]
   
    else:
      dp[i][j] = dp[i-1][j]
     
    
print(dp[n][target])

