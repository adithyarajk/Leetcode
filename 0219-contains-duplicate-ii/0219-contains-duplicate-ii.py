class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = dict()
        for index, ele in enumerate(nums):
            if hash_map.get(ele) is not None:
                if abs(hash_map.get(ele) - index) <= k:
                    return True
                else:
                    hash_map[ele] = index
            else:
                hash_map[ele] = index
        return False