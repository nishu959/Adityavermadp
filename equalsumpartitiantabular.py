
#gfg solution

def equalPartition(self, N, arr):
        if(sum(arr)%2!=0):
            return 0
        else:
            target = sum(arr)//2
            past = [[None for i in range(target+1)] for j in range(N+1)]

            for i in range(N+1):
                for j in range(target+1):  
    
                    if(i==0 and j!=0):
                        past[i][j] = 0
      
                    elif(j==0):
                        past[i][j] = 1
      
                    else:
                        if(j>=arr[i-1]):
                            past[i][j] = past[i-1][j-arr[i-1]] or past[i-1][j]
        
                        else:
                            past[i][j] = past[i-1][j]
            
            return past[N][target]