import collections
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        list1=[]
        freq=collections.Counter(arr)
        for val in freq.values():
            list1.append(val)
        print(list1)
        set1=set(list1)
        return len(set1)==len(list1)
