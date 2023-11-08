class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        map1 = []
        map2 = []
        for i in pattern:
            map1.append(pattern.index(i))
        for i in s:
            map2.append(s.index(i))
        if map1 == map2:
            return True
        return False