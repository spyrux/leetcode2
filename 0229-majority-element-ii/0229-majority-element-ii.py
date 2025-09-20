import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = collections.Counter(nums)
        results = []

        for key, value in counts.items():
            if value > (len(nums)//3):
                results.append(key)
        

        return results