# https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # depth fist search using recursion
        # if we find a a cell with a "1", do a dfs until we visit the whole island and
        # increment the areaCounter every time we move to the next cell with value "1"
        # Once we visit an entire island, compare the current areaCounter with the maxArea counter
        #return the max area counter
        # Time Complexity O(n*m) were n is number of rows and n number of columns
        visited = set() # keep track of the visited cells
        maxIslandArea = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLUMNS or (i,j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1)+ dfs(i, j+1)
        
        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                if grid[i][j] == 1 and ((i, j) not in visited):
                    currentIslandArea = dfs(i, j) #the number of cells of the whole island
                    maxIslandArea = max(currentIslandArea, maxIslandArea)
        return maxIslandArea

    # solve it also using iterative dfs