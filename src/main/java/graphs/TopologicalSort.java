package graphs;

import java.util.*;

public class TopologicalSort {
    public static void main(String[] args) {
        System.out.println(sort(5, new int[][]{
                {1,4},
                {2,4},
                {3,1},
                {3,2},
        }));
    }

    private static List<Integer> sort(int courses, int[][] required) {
        Queue<Integer> zeroIndeg = new LinkedList<>();
        List<Integer> sorted = new ArrayList<>();
        int[] indegrees = new int[courses];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        Map<Integer, List<Integer>> revGraph = new HashMap<>();
        for (int[] edge: required) {
            List<Integer> neighbors = graph.getOrDefault(edge[0], new ArrayList<>());
            neighbors.add(edge[1]);
            graph.put(edge[0], neighbors);

            neighbors = revGraph.getOrDefault(edge[1], new ArrayList<>());
            neighbors.add(edge[0]);
            revGraph.put(edge[1], neighbors);

            indegrees[edge[1]]++;
        }

        for (int i = 0; i < indegrees.length; i++) {
            if (indegrees[i] <= 0) zeroIndeg.add(i);
        }

        while (!graph.isEmpty() && !zeroIndeg.isEmpty()) {
            int u = zeroIndeg.poll();
            sorted.add(u);
            List<Integer> nodes = graph.getOrDefault(u, new ArrayList<>());
            graph.remove(u);
            for (int v: nodes) {
                List<Integer> fromNodes = revGraph.getOrDefault(v, new ArrayList<>());
                int i = 0;
                while (i < fromNodes.size()) {
                    if (fromNodes.get(i) == u) break;
                    i++;
                }
                fromNodes.remove(i);
                if (fromNodes.size() == 0) {
                    zeroIndeg.add(v);
                    revGraph.remove(v);
                }
            }
        }
        System.out.println(graph);
        System.out.println(revGraph);
        return sorted;
    }
}


