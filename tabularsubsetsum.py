n =int(input())

l = []


for i in range(n):
  l.append(int(input()))
 

target = int(input())

past = [[None for i in range(target+1)] for j in range(n+1)]


for i in range(n+1):
  for j in range(target+1):  
    
    if(i==0 and j!=0):
      past[i][j] = False
      
    elif(j==0):
      past[i][j] = True
      
    else:
      if(j>=l[i-1]):
        past[i][j] = past[i-1][j-l[i-1]] or past[i-1][j]
        
      else:
        past[i][j] = past[i-1][j]
        
        
        
print("true") if(past[n][target]) else print("false")
      
    
      
      