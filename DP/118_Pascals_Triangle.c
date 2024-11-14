class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp=[]
        for i in range(numRows):
            arr=[1]*(i+1)
            for j in range(1, i):
                arr[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp.append(arr)
        return dp

        
