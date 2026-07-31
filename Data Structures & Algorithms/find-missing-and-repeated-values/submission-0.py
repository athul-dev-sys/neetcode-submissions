class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d = {}

        for row in grid:
            for num in row:
                d[num] = d.get(num, 0) + 1

        size = len(grid) * len(grid)

        for i in range(1, size + 1):
            if d.get(i, 0) == 2:
                rep = i
            elif d.get(i, 0) == 0:
                mis = i

        return [rep, mis]