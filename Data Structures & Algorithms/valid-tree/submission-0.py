class Solution:
    def validTree(self, node_count: int, edges: List[List[int]]) -> bool:
        if node_count <= 0 and len(edges) > node_count - 1:
            return False

        adjacency_list = [[] for _ in range(node_count)]

        for source, destination in edges:
            adjacency_list[source].append(destination)
            adjacency_list[destination].append(source)

        visited = set()

        def dfs(current_node, parent_node):
            if current_node in visited:
                return False

            visited.add(current_node)

            for neighbor in adjacency_list[current_node]:
                if neighbor == parent_node:
                    continue

                if not dfs(neighbor, current_node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == node_count
