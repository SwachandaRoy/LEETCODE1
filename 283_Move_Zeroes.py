'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
      pos=0
      for i in range(len(nums)):
          if nums[i]!=0:
              nums[pos]=nums[i]
              pos+=1
      for i in range(pos, len(nums)):
          nums[i]=0
      return nums

