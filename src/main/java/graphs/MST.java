package graphs;

import graphs.util.Pair;

import java.util.*;

public class MST {

    static class Edge {
        int u;
        int v;
        int w;

        public Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }
    }

    public static void main(String[] args) {
        List<Edge> edges = new ArrayList<>();
        edges.add(new Edge(0, 1, 1));
        edges.add(new Edge(1, 2, 7));
        edges.add(new Edge(2, 3, 6));
        edges.add(new Edge(3, 4, 2));
        edges.add(new Edge(4, 0, 4));
        edges.add(new Edge(0, 2, 5));
        edges.add(new Edge(0, 3, 3));
        System.out.println(Kruskal(edges, 5));

        List<List<Pair>> adj = new ArrayList<>();
        adj.add(Arrays.asList(new Pair(1, 1), new Pair(2, 5), new Pair(3, 3)));
        adj.add(Arrays.asList(new Pair(2, 7)));
        adj.add(Arrays.asList(new Pair(3, 6)));
        adj.add(Arrays.asList(new Pair(4, 2)));
        adj.add(Arrays.asList(new Pair(0, 4)));
        WeightedGraph graph = new WeightedGraph(5, adj);
        System.out.println(Prims(graph));
    }

    private static int find(int[] parent, int u) {
        if (parent[u] == u) return u;
        return find(parent, parent[u]);
    }

    private static void union(int[] parent, int[] countSet, int u, int v) {
        if (countSet[u] >= countSet[v]) {
            parent[v] = u;
            countSet[u] += countSet[v];
        } else if (countSet[u] < countSet[v]) {
            parent[u] = v;
            countSet[v] += countSet[u];
        }
    }

    private static int Kruskal(List<Edge> edges, int nodes) {
        int[] parent = new int[nodes];
        int[] countSet = new int[nodes];
        for (int i = 0; i < parent.length; i++) {
            parent[i] = i;
        }
        edges.sort(Comparator.comparingInt(e -> e.w));
        int cost = 0;
        for (Edge e : edges) {
            int parentU = find(parent, e.u);
            int parentV = find(parent, e.v);
            if (parentU == parentV) continue;
            union(parent, countSet, parentU, parentV);
            cost += e.w;
        }
        return cost;
    }

    private static int Prims(WeightedGraph graph) {
        boolean[] visited = new boolean[graph.getV()];
        Queue<Pair> queue = new PriorityQueue<>(Comparator.comparingInt(o -> o.second));
        queue.add(new Pair(0, 0));
        int cost = 0;
        while (!queue.isEmpty()) {
            Pair item = queue.poll();
            if (visited[item.first]) continue;
            visited[item.first] = true;
            cost += item.second;
            for (Pair p : graph.getNeighbours(item.first)) {
                if (visited[p.first]) continue;
                queue.add(new Pair(p.first, p.second));
            }
        }
        return cost;
    }
}
