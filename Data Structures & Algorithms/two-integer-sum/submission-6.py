class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # make a hashmap that tracks indices and values 

        # seen sets can be built progressively 

        track = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in track:
                return [track[diff], i]
            track[v] = i
        
            


