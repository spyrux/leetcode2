from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in range(len(s)):
            count1[s[i]]+=1

        for i in range(len(t)):
            count2[t[i]]+=1

        
        return count1 == count2