from collections import deque, defaultdict


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda : {"red" : [], "blue" : []})

        for u, v in redEdges:
            graph[u]["red"].append(v)

        for u, v in blueEdges:
            graph[u]["blue"].append(v)

        result = [-1] * n
        queue = deque([(0, "red", 0), (0, "blue", 0)])
        visited = {(0, "red"), (0, "blue")}

        while queue:

            node, color, distance = queue.popleft()
            if result[node] == -1:
                result[node] = distance
            next_color = "blue" if color == "red" else "red"

            for neighbour in graph[node][next_color]:
                if (neighbour, next_color) not in visited:
                    visited.add((neighbour, next_color))
                    queue.append((neighbour, next_color, distance +1))
        return result