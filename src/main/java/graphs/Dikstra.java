package graphs;

import graphs.util.Pair;

import java.io.*;
import java.util.*;

/**
 * Dikstra's algorithm is used to find out the shortest distance of all other nodes from a given node in a weighted
 * graph.
 * <p>
 * Algorithm works as follows:
 * Let's call the given node as source node.
 * The idea is to maintain distances array for each node from the source node
 * We start off by marking all nodes in the graph at infinite distance from source node
 * and we mark source node at distance 0 as that shall be the starting point
 * <p>
 * Then assuming we are at a given node for which we have already calculated the minimum distance from source
 * the minimum distance for it's neighbours shall be following:
 * minDestDist = min. distance of neighbours from source
 * minCurrDist = min. distance at current node from source
 * weightCurrDest = weight of graph edge from current to destination
 * <p>
 * if
 * minDestDist > minCurrDist + weightCurrDest
 * then,
 * minDestDist = minCurrDist + weightCurrDest
 * else,
 * do nothing
 * <p>
 * We need to ensure that the minimum distance calculated here is also considered for next neighbours
 * Only the minimum distance should be propagated further.
 * <p>
 * Hence we shall use priority queue to insert minimum distance every time we find one and use it for subsequent
 * neighbours. The item in the queue shall be (distance, node). The priority queue shall be sorted by shortest to largest
 * distance in increasing order.
 * <p>
 * Summary:
 * 1. insert (0, source node) in priority queue
 * 2. iterate as long as queue is not empty
 * 3. poll first element from queue (this should have the minimum distance propagated from previous neighbours)
 * 4. Use the current minimum distance to update distances for neighbours
 * 5. insert into priority queue
 * 6. repeat
 */
public class Dikstra {

    private final List<List<Pair>> edges;
    private final int[] distances;

    public Dikstra(int nodes, int edges) {
        this.edges = new ArrayList<>();
        this.distances = new int[nodes];
        for (int i = 0; i < edges; i++) {
            this.edges.add(new ArrayList<>());
        }
    }

    public void addEdge(int u, Pair p) {
        this.edges.get(u).add(p);
    }

    public int[] calculateShortestPath(int source) {
        for (int i = 0; i < distances.length; i++) {
            this.distances[i] = Integer.MAX_VALUE;
        }
        this.distances[source] = 0;
        boolean[] visited = new boolean[distances.length];
        PriorityQueue<Pair> q = new PriorityQueue<>(Comparator.comparingInt(p -> p.first));
        q.add(new Pair(0, 0));

        while (!q.isEmpty()) {
            Pair src = q.poll();
            if (visited[src.second]) continue;
            visited[src.second] = true;
            for (Pair dest : edges.get(src.second)) {
                if (dest.first + distances[src.second] < distances[dest.second]) {
                    distances[dest.second] = dest.first + distances[src.second];
                    q.add(new Pair(distances[dest.second], dest.second));
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
                Dikstra.class.getClassLoader().getResourceAsStream("shortest-dist-input.txt"));
        BufferedReader br = new BufferedReader(is);
        String bounds = br.readLine();
        String[] boundaries = bounds.split(" ");

        int n = Integer.parseInt(boundaries[0]);
        int m = Integer.parseInt(boundaries[1]);

        Dikstra dik = new Dikstra(n, m);
        for (int i = 0; i < m; i++) {
            String edgeStr = br.readLine();
            if (edgeStr == null || edgeStr.isEmpty()) continue;
            String[] edge = edgeStr.split(" ");
            int u = Integer.parseInt(edge[0]) - 1;
            int v = Integer.parseInt(edge[1]) - 1;
            int w = Integer.parseInt(edge[2]);
            dik.addEdge(u, new Pair(w, v));
        }

        System.out.println(Arrays.toString(dik.calculateShortestPath(0)));
    }
}
