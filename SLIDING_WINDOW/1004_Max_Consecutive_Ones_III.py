class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=maxcount=0
        l, r=0, 0
        n=len(nums)
        for r in range(n):
            if nums[r]==1:
                r+=1
                count+=1
            else:
                if k>0:
                    r+=1
                    k-=1
                    count+=1
                else:
                    while nums[l]==1:
                        l+=1
                        count-=1
                    l+=1
            maxcount=max(maxcount, count)
                        
        return maxcount
