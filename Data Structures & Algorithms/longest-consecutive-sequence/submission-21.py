class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
            
        nums = set(nums)

        longest = 1

        for i in nums:
            if i - 1 not in nums:
                n = 1
                while i + n in nums:
                    n += 1
                longest = max(n, longest)
        
        return longest

