class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort so we can use two pointers
        #sliding window does not work on this 
        #need to use two pointers in a for loop
        nums.sort()
        result = []
        unique = set()
        n = len(nums)
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                if nums[i]+ nums[left]+nums[right] == 0:
                    unique.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[i]+ nums[left]+nums[right] < 0:
                    left += 1
                else:
                    right-=1


        return list(unique)