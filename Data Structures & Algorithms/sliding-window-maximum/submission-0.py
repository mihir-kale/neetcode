class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        q = deque()
        l = r = 0 

        while r < len(nums):
            r = l + k
            output.append(max(nums[l:r]))
            l += 1
        
        return output