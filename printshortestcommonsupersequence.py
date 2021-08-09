x =input()
y = input()


a = len(x)
b = len(y)

dp = [[None for i in range(b+1)]for j in range(a+1)]

for i in range(a+1):
  for j in range(b+1):
    
    dp[i][j] = 0
    
    
for i in range(1,a+1):
  for j in range(1,b+1):
    
    if(x[i-1]==y[j-1]):
      dp[i][j] = dp[i-1][j-1] + 1
      
      
    else:
      dp[i][j] = max(dp[i][j-1],dp[i-1][j])
      
     
 
i = a
j = b

ans = ""


while(i>0 and j>0):
  
  if(x[i-1]==y[j-1]):
    ans += x[i-1]
    i-=1
    j-=1
    
  else:
    
    if(dp[i-1][j] > dp[i][j-1]):
      ans += x[i-1]
      i-=1
      
    elif(dp[i][j-1] > dp[i-1][j]):
      ans += y[j-1]
      j-=1
      
   
while(i>0):
  ans += a[i-1]
  i-=1
  

while(j>0):
  ans += a[j-1]
  j-=1
  
  
print(ans[::-1])
  
    
  
    
    
    

    