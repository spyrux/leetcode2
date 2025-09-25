class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        count_map = {}
        prefix = 0

        for right in range(len(nums)):
            if nums[right] in count_map:
                count_map[nums[right]]+=1
            else:
                count_map[nums[right]] = 1

            if len(count_map) > k:
                while len(count_map) > k:
                    if count_map[nums[left]] > 1:
                        count_map[nums[left]] -= 1
                    else:
                        count_map.pop(nums[left])
                    left+=1
                    prefix = 0
        
            while len(count_map) == k and count_map[nums[left]] > 1:

                count_map[nums[left]] -= 1
                left+=1
                prefix+=1
            
            if len(count_map) == k:
                count+=prefix+1

                
        return count