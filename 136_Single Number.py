class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in range(1, len(A)):
            ans = ans ^ A[i]
        return ans
    
'''   
A=[1,1,2,2,3,4,4,5,5]
B=Solution.singleNumber(Solution,A)
print B
'''
