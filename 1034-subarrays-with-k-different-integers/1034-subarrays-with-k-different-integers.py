from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        count_map = defaultdict(int)
        prefix = 0

        for right in range(len(nums)):
            count_map[nums[right]] += 1

            # shrink until we have at most k distinct
            if len(count_map) > k:
                while len(count_map) > k:
                    count_map[nums[left]] -= 1
                    if count_map[nums[left]] == 0:
                        count_map.pop(nums[left])
                    left += 1
                prefix = 0  # reset prefix because we just dropped below k

            # slide left over duplicates while keeping k distinct
            while len(count_map) == k and count_map[nums[left]] > 1:
                count_map[nums[left]] -= 1
                left += 1
                prefix += 1

            if len(count_map) == k:
                count += prefix + 1  # all subarrays ending at right

        return count