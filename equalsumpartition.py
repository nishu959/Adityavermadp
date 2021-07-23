#gfg solution
class Solution:
    def equalPartition(self, N, arr):
        if(sum(arr)%2!=0):
            return 0
        else:
            return self.subsetsum(N, sum(arr)//2, arr)
            
            
    def subsetsum(self,n, target, arr):
  
        if(n==0):
            return 0
 
        if(target ==0):
            return 1
  
        if(arr[n-1]<=target):
            ans= self.subsetsum(n-1, target-arr[n-1], arr)  or self.subsetsum(n-1, target, arr)  
            return ans
            
        else:
            ans = self.subsetsum(n-1, target, arr)
            return ans