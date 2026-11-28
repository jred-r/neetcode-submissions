from collections import deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for src, tgt in edges:
            adj[src].append(tgt)
            adj[tgt].append(src)
        
        visited = set()
        count = 0

        def bfs(node):
            visited.add(node)
            queue = deque([node])
            while queue:
                current = queue.popleft()
                for nbr in adj[current]:
                    if nbr in visited:
                        continue
                    visited.add(nbr)
                    queue.append(nbr)
        
        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1
        
        return count
        