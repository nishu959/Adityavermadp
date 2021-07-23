
n =int(input())

l = []


for i in range(n):
  l.append(int(input()))
  
  
 

target = int(input())

past = [[None for i in range(target+1)] for j in range(n+1)]

def subsetsum(n, target, past):
  if(target ==0):
    past[n][target] = True
    
    return True
  
  if(n==0):
    past[n][target] = False 
    return False
 
  
  
  if(past[n][target]!=None):
    return past[n][target]
    
  if(l[n-1]<=target):
    ans= subsetsum(n-1, target-l[n-1], past)  or subsetsum(n-1, target, past)  
    past[n][target] = ans
    return ans
  else:
    
    ans = subsetsum(n-1, target, past)
    past[n][target] = ans
    return ans
 
 
print("true") if(subsetsum(n, target, past)) else print("false")



