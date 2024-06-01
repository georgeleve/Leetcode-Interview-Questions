# https://leetcode.com/problems/max-area-of-island/description/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Iterative dfs using a stack
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set()
        maxIslandArea = 0
        def dfs(i, j):
            #print("we found a new island")
            stack = []
            stack.append((i,j))
            currentIslandArea = 1
            visited.add((i,j))
            #print(i , "," , j)
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc
                    if (r >= 0 and r < ROWS and c >= 0 and c < COLUMNS and (r, c) not in visited and grid[r][c] == 1):
                        #print(r , "," , c)
                        stack.append((r, c))
                        visited.add((r, c))
                        currentIslandArea += 1
            return currentIslandArea

        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                if grid[i][j] == 1 and (i,j) not in visited:
                    currentIslandArea = dfs(i,j)
                    #print("currentIslandArea=", currentIslandArea)
                    maxIslandArea = max(currentIslandArea, maxIslandArea)
        return maxIslandArea
        
    def maxAreaOfIsland2222(self, grid: List[List[int]]) -> int:
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

        def dfs2(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLUMNS or (i,j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1)+ dfs(i, j+1)
        
        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                if grid[i][j] == 1 and ((i, j) not in visited):
                    currentIslandArea = dfs2(i, j) #the number of cells of the whole island
                    maxIslandArea = max(currentIslandArea, maxIslandArea)
        return maxIslandArea