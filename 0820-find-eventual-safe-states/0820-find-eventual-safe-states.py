class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if state[node] != 0:
                return state[node] == 2
            state[node] = 1

            for neighbour in graph[node]:
                if not dfs(neighbour):
                    return False
            state[node] = 2
            return True

        n = len(graph)
        state = [0] * n

        safe_nodes = []
        for vertex in range(n):
            if dfs(vertex):
                safe_nodes.append(vertex)
        return safe_nodes