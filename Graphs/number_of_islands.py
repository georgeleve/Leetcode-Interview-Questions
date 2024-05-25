# Solution with Iterative DFS using a stack:
class Solution:
    # O(n*m) Time Complexity | O(n*m) Space Compelxity | Breadth First Search
    def numIslands(self, grid):
        if grid is None or len(grid[0]) is None:
            return 0
        numberOfIslands = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set() #keep track of the visited cells
        
        def bfs(i, j):
            stack = []
            stack.append((i, j))
            visited.add((i, j))
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            while stack:
                currentRow, currentColumn = stack.pop()  
                for dr, dc in directions:
                    row = currentRow + dr
                    col = currentColumn + dc
                    if (row in range(ROWS) and
                        col in range(COLUMNS) and
                        grid[row][col] == "1" and
                        (row, col) not in visited):
                            stack.append((row, col))
                            visited.add((row, col))

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    visited.add((i,j))
                    numberOfIslands += 1
        return numberOfIslands

'''
class Solution:
    #Recursive DFS
    # O(n*m) Time Complexity | O(n*m) Space Compelxity, where n is the number of rows and m is the number of columns
    def numIslands(self, grid):
        if (grid is None) or (grid[0] is None):
            return 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        numberOfIslands = 0
        visited = set() # Keep track of the already visited places so we don't get stuck in endless loop

        def dfs(i, j):
            if (i not in range(0, ROWS)
                or j not in range(0, COLUMNS)
                or (i,j) in visited
                or grid[i][j] == "0"):
                    return
            visited.add((i, j)) #add a tuple to the set
            directions =[[0,1], [1,0], [0,-1], [-1,0]]
            for r, c in directions:
                dfs(i + r, j + c)

        for i in range(0, ROWS):
            for j in range(0, COLUMNS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    visited.add((i,j)) 
                    numberOfIslands += 1 # after each dfs we visited a new island so we inscrement the counter
        return numberOfIslands                

# Solution with BFS using a queue:
class Solution:
    # O(n*m) Time Complexity | O(n*m) Space Compelxity | Breadth First Search
    def numIslands(self, grid):
        if grid is None or len(grid[0]) is None:
            return 0
        numberOfIslands = 0
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set() #keep track of the visited cells
        
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))
            directions = [[0,1], [1,0], [0,-1], [-1,0]]
            while queue:
                currentRow, currentColumn = queue.popleft()  
                for dr, dc in directions:
                    row = currentRow + dr
                    col = currentColumn + dc
                    if (row in range(ROWS) and
                        col in range(COLUMNS) and
                        grid[row][col] == "1" and
                        (row, col) not in visited):
                            queue.append((row, col))
                            visited.add((row, col))

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i, j)
                    visited.add((i,j))
                    numberOfIslands += 1
        return numberOfIslands
'''