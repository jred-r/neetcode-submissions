"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        nodes = {}
        seen = set()

        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            nodes[node] = Node(val=node.val)
            for nbr in node.neighbors:
                dfs(nbr)

        dfs(node)
        for nd, clone in nodes.items():
            for nbr in nd.neighbors:
                clone.neighbors.append(nodes[nbr])

        return nodes[node]
