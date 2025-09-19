class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #NO NEED FOR BINARY SEARCH TO FIND FIRST POINT BECAUSE WE CAN JUST ITERATE AND COMPARE BOUNDS
        #iterate thru the list to merge any overlapping with new interval
        if not intervals:
            return [newInterval]
        result = []
        back = []
        min_start, max_end = newInterval

        for interval in intervals:
            if interval[1] < min_start:
                result.append(interval)
            elif (interval[0] <= min_start and interval[1] >= min_start) or (interval[0] <= max_end):
                min_start = min(min_start, interval[0])
                max_end = max(max_end, interval[1])
            elif interval[0] > max_end:
                back.append(interval)
        
        result.append([min_start, max_end])

        result+=back
        return result
            



             