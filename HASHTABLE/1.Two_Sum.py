import collections
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d=defaultdict(int)
        for indx, dig in enumerate(nums):
            complement=target-dig
            if complement in d.keys():
                return [indx, d[complement]]
            else:
                d[dig]=indx
            
