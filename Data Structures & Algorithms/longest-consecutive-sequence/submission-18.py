class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        glob = 0

        for i in nums:
            if i - 1 not in nums:
                n = 1
                while i + n in nums:
                    n += 1 
                loc = n
                glob = max(glob, loc)
        
        return glob