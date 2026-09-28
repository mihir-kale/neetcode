class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        longest = 1

        if not nums:
            return 0
            
        for i in nums:
            if i - 1 not in nums: 
                count = 1
                while i + count in nums:
                    count += 1
                longest = max(longest, count)
        

        return longest
