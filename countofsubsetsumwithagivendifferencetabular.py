n = int(input())

l = list(map(int, input().split()))

diff = int(input())

s = sum(l) + diff

target = s//2

dp = [[None for i in range(target+1)] for j in range(n+1)]


for i in range(n+1):
  for j in range(target+1):
    
    if(i==0):
      dp[i][j] = 0
   
    if(j==0):
      dp[i][j] = 1
     
for i in range(1,n+1):
  for j in range(1,target+1):
   
    if(j>= l[i-1]):
      dp[i][j] = dp[i-1][j] + dp[i-1][j-l[i-1]]
     
    else:
      dp[i][j] = dp[i-1][j]
     
    
print(dp[n][target])

