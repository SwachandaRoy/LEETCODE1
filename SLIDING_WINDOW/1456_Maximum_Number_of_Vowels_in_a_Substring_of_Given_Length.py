class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vcount=0
        i=0
        j=k-1
        n=len(s)
        vowel='aeiouAEIOU'
        for char in s[0:k]:
            if char in vowel:
                vcount+=1
        maxcount=vcount
        while j<n-1:
            j+=1
            i+=1
            if s[i-1] in vowel:
                vcount-=1
            if s[j] in vowel:
                vcount+=1
            maxcount=max(maxcount, vcount)
        return maxcount

        
