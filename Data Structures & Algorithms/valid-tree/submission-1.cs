public class Solution {
    public bool ValidTree(int n, int[][] edges) {
        if (n <= 0 || edges.Length > n - 1) {
            return false;
        }

        List<List<int>> adjLst = [];
        for (int i = 0; i < n; i++) {
            adjLst.Add([]);
        }

        foreach (var edge in edges) {
            adjLst[edge[0]].Add(edge[1]);
            adjLst[edge[1]].Add(edge[0]);
        }

        Queue<(int, int)> queue = [];
        queue.Enqueue((0, -1));
        HashSet<int> visited = [];
        visited.Add(0);
        while (queue.Count > 0) {
            (int node, int parent) = queue.Dequeue();
            foreach (int nbr in adjLst[node]) {
                if (nbr == parent) {
                    continue;
                }

                if (visited.Contains(nbr)) {
                    return false;
                }

                visited.Add(nbr);
                queue.Enqueue((nbr, node));
            }
        }

        return visited.Count == n;
    }
}
