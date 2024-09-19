class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        subs=[]
        def backtracking(i):
            
            if i>=len(nums):
                res.append(subs[:])
                return

            subs.append(nums[i])
            backtracking(i+1)
            subs.pop()
            backtracking(i+1)

        backtracking(0)
        return res
