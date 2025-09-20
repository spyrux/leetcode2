import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        maj = nums[0]
        max_count = counts[maj]

        for key, value in counts.items():
            if value > counts[maj]:
                maj = key
                max_count = value
        

        return maj