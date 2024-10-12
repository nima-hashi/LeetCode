class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        
        intervals = []
        ans = []
        max_height = 0
        
        for pos in positions:
            left, size = pos
            right = left + size
            base_height = 0
            
            # Find the maximum height in the range where the new square will fall
            for l, r, h in intervals:
                if not (right <= l or left >= r):  # check if current interval overlaps
                    base_height = max(base_height, h)
            
            # The new square height is based on the current max height of overlapping intervals
            new_height = base_height + size
            intervals.append((left, right, new_height))
            max_height = max(max_height, new_height)
            ans.append(max_height)
        
        return ans