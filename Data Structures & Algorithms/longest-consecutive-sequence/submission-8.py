class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sorted vs set - sorted is clean but not necessary

        nset = set(nums)
        ret = 0

        for i in nset:
            if (i - 1) not in nset:
                count = 1
                while (i + count) in nset:
                    count += 1
                ret = max(ret, count)
        
        return ret
        