x = input()
y = input()

a = len(x)
b = len(y)

dp = [[None for i in range(b+1)] for j in range(a+1)]



for i in range(a+1):
  for j in range(b+1):
    
    if(i==0 or j==0):
      
      dp[i][j]  = 0
     
   
for i in range(1,a+1):
  for j in range(1,b+1):
   
    if(x[i-1]==y[j-1]):
      dp[i][j] = 1+ dp[i-1][j-1]
     
    else:
      dp[i][j] = max(dp[i][j-1],dp[i-1][j])
     
    
print(dp[a][b])