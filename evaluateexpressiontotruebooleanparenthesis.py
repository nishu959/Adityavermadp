s= input()

dp = {}


def solve(s, i, j, torf):
  
  if(i>j):
    return 0
   
  if(i==j):
    if(torf == True):
      return (s[i]=="T")
     
    else:
      return (s[i]=="F")
      
  temp = str(i)+" "+str(j)+" "+ str(torf)
  
  
  if temp in dp:
    return dp[temp]
  
  
  
  ans = 0   
  for k in range(i+1,j, 2):
    
    lt = solve(s, i, k-1, True)
    lf = solve(s, i, k-1, False)
    
    rt = solve(s, k+1, j, True)
    rf = solve(s, k+1, j, False)
   
    if(s[k]=="&"):
      
      if(torf==True):
        ans += lt * rt
        
      else:
        ans += lf * rf + lt * rf + lf * rt
    
      
    elif(s[k]=="|"):
      
      if(torf==True):
        ans += lt * rt + lt * rf + lf * rt
        
      else:
        ans += lf * rf
     
        
    elif(s[k]=="^"):
      
      if(torf==True):
        ans += lt * rf + lf * rt
        
      else:
        ans += lf * rf + lt * rt
        
  
  dp[temp] = ans
        
  return ans
  
  
print(solve(s, 0, len(s)-1, True))



        
    