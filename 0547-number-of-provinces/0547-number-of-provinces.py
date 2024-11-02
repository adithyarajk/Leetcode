class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(node):
            visited[node] = True

            for neighbour in range(n):
                if not visited[neighbour] and isConnected[node][neighbour] == 1:
                    dfs(neighbour)

        n = len(isConnected)
        provinces_count = 0
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces_count+=1

        return provinces_count
