class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            hash_table[sorted_word].append(word)

        return list(hash_table.values())       