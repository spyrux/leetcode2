class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we want to track the length of the longest substring by using a sliding window approach 
        #we use a hashmap to track duplicates 
        #when we encounter a duplicate we need to move the left side of the sliding window until we do not have a duplicate and remove chars
        left = 0
        longest = 0
        seen_map = {}

        for i in range(0, len(s)):
            if s[i] not in seen_map:
                seen_map[s[i]] = i
            else:
                while s[i] in seen_map:
                    seen_map.pop(s[left])
                    left+=1
                seen_map[s[i]] = i
            longest = max(longest, len(seen_map))
        
        return longest
        