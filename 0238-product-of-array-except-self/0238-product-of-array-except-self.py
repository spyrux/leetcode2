class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in range(len(nums))]
        right = [1 for i in range(len(nums))]

        for i in range(len(nums)-2, -1,-1):
            right[i] = nums[i+1]*right[i+1]
        for i in range(1, len(nums)):
            left[i] = nums[i-1]*left[i-1]
        
        product = [right[i]*left[i] for i in range(len(nums))]

        return product