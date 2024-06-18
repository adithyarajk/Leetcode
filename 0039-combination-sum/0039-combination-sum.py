class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 0:
                result.append(path)
                return
            elif target < 0:
                return
            else:
                for index in range(start, len(candidates)):
                    backtrack(index, target-candidates[index], [candidates[index]]+ path, result)
        result = []
        candidates.sort()
        backtrack(0, target, [], result)
        return result
