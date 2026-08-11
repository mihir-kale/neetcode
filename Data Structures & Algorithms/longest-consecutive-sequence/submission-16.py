class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # nums = [2,20,4,10,3,4,5]
        nums.sort() # nums  = [2, 3, 4, 4, 5, 10, 20]
        nums = set(nums)
        res = 0

        for i in nums:

            if i - 1 not in nums:

                length = 1

                while i + length in nums: 

                    length += 1
                

                res = max(res, length)
        
        return res
