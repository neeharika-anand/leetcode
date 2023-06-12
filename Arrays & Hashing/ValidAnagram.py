class Solution(object):
    def isAnagram(self, s, t):
        # Brute Force with O(1) space complexity 
        # a=sorted(s)
        # b=sorted(t)
        # return a==b

        #Using Hashmaps
        if len(s)!=len(t):
            return False
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        return countS==countT