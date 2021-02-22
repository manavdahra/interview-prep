package graphs;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class BellmanFord {

    static class Edge {
        int u;
        int v;
        int w;

        Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }

        public String toString() {
            return "(" + this.u + ", " + this.v + ", " + this.w + ")";
        }
    }

    private final List<Edge> edges;
    private final int[] distances;

    public BellmanFord(int nodes) {
        this.edges = new ArrayList<>();
        this.distances = new int[nodes];
    }

    public void addEdge(Edge e) {
        this.edges.add(e);
    }

    public int[] calculateShortestPath(int source) {
        for (int i = 0; i < distances.length; i++) {
            this.distances[i] = Integer.MAX_VALUE;
        }
        this.distances[source] = 0;
        for (int i = 0; i < distances.length; i++) {
            for (Edge edge : edges) {
                if (edge.w + distances[edge.u] < distances[edge.v]) {
                    distances[edge.v] = edge.w + distances[edge.u];
                }
            }
        }
        return distances;
    }

    public static void main(String[] args) throws IOException {
        StringReader reader = new StringReader("5 5\n" +
                "1 2 5\n" +
                "1 3 2\n" +
                "3 4 1\n" +
                "1 4 6\n" +
                "3 5 5");
        InputStreamReader is = new InputStreamReader(
                BellmanFord.class.getClassLoader().getResourceAsStream("shortest-dist-input.txt"));
        BufferedReader br = new BufferedReader(is);
        String bounds = br.readLine();
        String[] boundaries = bounds.split(" ");

        int n = Integer.parseInt(boundaries[0]);
        int m = Integer.parseInt(boundaries[1]);

        BellmanFord bf = new BellmanFord(n);
        for (int i = 0; i < m; i++) {
            String edgeStr = br.readLine();
            if (edgeStr == null || edgeStr.isEmpty()) continue;
            String[] edge = edgeStr.split(" ");
            int u = Integer.parseInt(edge[0])-1;
            int v = Integer.parseInt(edge[1])-1;
            int w = Integer.parseInt(edge[2]);
            bf.addEdge(new Edge(u, v, w));
        }

        System.out.println(Arrays.toString(bf.calculateShortestPath(0)));
    }
}
