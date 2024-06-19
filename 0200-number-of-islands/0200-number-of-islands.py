class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = "#"
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for direction in directions:
                index_x = i+direction[0]
                index_y = j+direction[1]
                if index_x >= 0 and index_y>=0 and index_x < len(grid) and index_y < len(grid[0]):
                    if grid[index_x][index_y] == "1":
                        dfs(index_x, index_y)
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    count+=1
                    dfs(x, y)
        return count