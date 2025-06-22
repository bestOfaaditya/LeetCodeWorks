class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_freq = {}
        count = 0
        for i, row in enumerate(grid):
            t = tuple(row)
            if t not in row_freq:
                row_freq[t] = 1
            else:
                row_freq[t] += 1
        
        for j in range(0, len(grid)):
            column = tuple([row[j] for row in grid])
            if column in row_freq:
                count += row_freq[column]
        return count
        
