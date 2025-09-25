class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #this is dfs with backtracking
        #at each index we can choose to either add itself or add next index
        #if it is greater than target we stop
        sums = []

        def dfs(currList, currSum, index):
            if currSum > target:
                return
            if currSum == target:
                sums.append(currList)
            for i in range(index, len(candidates)):
                new_list = [i for i in currList]
                new_list.append(candidates[i])
                dfs(new_list, currSum+candidates[i], i)
        
        dfs([],0,0)

        return sums


            