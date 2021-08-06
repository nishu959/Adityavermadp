n = int(input())

length = list(map(int, input().split()))


price = list(map(int, input().split()))

dp = [[None for i in range(n+1)] for j in range(n+1)]


for i in range(n+1):
  for j in range(n+1):
    
    if(i==0 or j==0):
      dp[i][j] = 0
     
    
for i in range(1,n+1):
  for j in range(1,n+1):
    
    if(j >= length[i-1]):
      dp[i][j] = max(price[i-1] + dp[i][j-length[i-1]], dp[i-1][j])
      
    else:
      dp[i][j] = dp[i-1][j]
      
      
      
print(dp[n][n])
  
   
    