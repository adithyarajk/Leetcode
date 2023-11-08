class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = dict()
        magazine_dict = dict()
        
        for m in magazine:
            if magazine_dict.get(m) == None:
                magazine_dict[m] = 1
            else:
                magazine_dict[m] += 1
        for m in ransomNote:
            if ransomNote_dict.get(m) == None:
                ransomNote_dict[m] = 1
            else:
                ransomNote_dict[m] += 1
        for key, value in ransomNote_dict.items():
            if magazine_dict.get(key) == None or magazine_dict[key] < value:
                return False
        return True
