class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):

            visited[node] = True
            for neighbour in rooms[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        n = len(rooms)
        visited = [False] * n
        dfs(0)
        return all(visited)