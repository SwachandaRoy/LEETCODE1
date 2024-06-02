class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1=len(word1)
        len2=len(word2)
        word3=[]
        i=0
        j=0
        while i<len1 and j<len2:
            word3.append(word1[i])
            word3.append(word2[j])
            i+=1
            j+=1

        if len1>len2:
            while i<len1:
                word3.append(word1[i])
        else:
            while j<len2:
                word3.append(word2[j])
                
        word3=''.join(word3)
        return word3
