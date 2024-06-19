class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=s.split()
        ls.reverse()
        s=" ".join(ls)
        return s
