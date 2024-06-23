class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i=0
        n=len(nums)
        j=k-1
        maxsum=cursum=sum(nums[0:k])
        while j<n-1:
            j+=1
            i+=1
            cursum+=(nums[j]-nums[i-1])
            maxsum=max(maxsum, cursum)
        return maxsum/float(k)
