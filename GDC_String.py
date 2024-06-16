class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        if str1+str2!=str2+str1:
            return ""
        l1=len(str1)
        l2=len(str2)
        lg=gcd(l1, l2)
        print(lg)
        return str1[0:lg]
