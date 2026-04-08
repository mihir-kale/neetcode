class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comps = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in comps:
                return [comps[diff], i] # smaller first
            comps[n] = i
