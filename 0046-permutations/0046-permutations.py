class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #dfs with every index add if its not seen
        #add to perms when lengths are equal
        perms = []
        visited = set()
        def dfs(currList, visited, index):
            if len(currList) > len(nums):
                return
            if len(currList) == len(nums):
                perms.append(currList)
            for i in range(len(nums)):
                if i not in visited:
                    newList = [x for x in currList]
                    newList.append(nums[i])
                    visited.add(i)
                    dfs(newList, visited, i)
                    visited.remove(i)
    
        dfs([],visited,0)
        return perms
            