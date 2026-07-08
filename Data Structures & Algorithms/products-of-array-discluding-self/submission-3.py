class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        zeros = 0
        ret = [0] * len(nums)

        for i in nums:
            if i != 0:
                prod *= i
            else:
                zeros += 1
        
        if zeros == 0: # no zeroes, clean
            for i in range(len(nums)):
                ret[i] = prod // nums[i] 
        elif zeros == 1: # 1 zero - only that zero will have val
            for i in range(len(nums)):
                if nums[i] == 0:
                    ret[i] = prod
        return ret # more than 1 zero, all vals are 0




