n =int(input())

l = []


for i in range(n):
  l.append(int(input()))
 

target = int(input())

past = [[None for i in range(target+1)] for j in range(n+1)]


for i in range(n+1):
  for j in range(target+1):  
    
    if(i==0 and j!=0):
      past[i][j] = 0
      
    elif(j==0):
      past[i][j] = 1
      
    else:
      if(j>=l[i-1]):
        past[i][j] = past[i][j-l[i-1]] + past[i-1][j]
        
      else:
        past[i][j] = past[i-1][j]
        
        
        
print(past[n][target]) 
      
    
      