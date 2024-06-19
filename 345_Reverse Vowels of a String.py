class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        alph='aeiouAEIOU'
        i=0
        j=len(s)-1
        slist=list(s)
        while i<j:
            if slist[i] in alph:
                if slist[j] in alph:
                    slist[i], slist[j]=slist[j], slist[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        s="".join(slist)
        return s

        
