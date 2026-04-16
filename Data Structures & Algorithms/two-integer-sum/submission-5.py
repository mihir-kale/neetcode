class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        track = {}

        for i, n in enumerate(nums):
            hit = target - n 
            if hit in track:
                return [track[hit], i]
            track[n] = i 