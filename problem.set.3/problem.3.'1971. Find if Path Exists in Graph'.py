class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        vis = [0 for i in range(n)]

        graph = [[] for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(start, end):

            if start == end:
                return True

            queue = [start]
            vis[start] = 1

            while queue:

                node = queue.pop()
                for neighbour in graph[node]:

                    if neighbour == end:
                        return True

                    if vis[neighbour] == 0:
                        vis[neighbour] = 1
                        queue.append(neighbour)
            
            return False
        
        return bfs(source, destination)