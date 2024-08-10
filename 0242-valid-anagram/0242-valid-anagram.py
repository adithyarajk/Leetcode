class Solution(object):
    def createDict(self, s):
        counter = dict()

        for i in s:
            if counter.get(i):
                counter[i]=counter.get(i) +1
            else:
                counter[i]=1
        return counter

    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = self.createDict(s)
        dict2 = self.createDict(t)
        for i in s:
            if dict1.get(i)!=dict2.get(i):
                return False
        for i in t:
            if dict1.get(i)!=dict2.get(i):
                return False

        return True