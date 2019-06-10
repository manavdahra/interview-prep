package graphs;

import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Author: B0204046
 * Date: 26/08/18 11:39
 */
public class Graph {

    private int V;

    private List<Integer>[] adj;

    public Graph(int v) {
        V = v;
        adj = new List[v];
        for (int i = 0; i < v; i++) {
            adj[i] = new LinkedList<>();
        }
    }

    public void addEdge(int v, int w) {
        adj[v].add(w);
    }

    public void DFS(int v, boolean[] visited) {
        System.out.print(v + " ");
        visited[v] = true;
        List<Integer> vertices = adj[v];
        for (int vertex : vertices) {
            if (visited[vertex]) {
                continue;
            }

            DFS(vertex, visited);
        }
    }

    public void DFS(boolean[] visited) {
        for (int i = 0; i < adj.length; i++) {
            if (visited[i]) {
                continue;
            }
            System.out.println("\n------");
            DFS(i, visited);
        }
    }

    public void BFS(int v, boolean[] visited) {
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(v);
        visited[v] = true;
        System.out.print(v + " ");
        while (!queue.isEmpty()) {
            int vertex = queue.remove();
            List<Integer> neighbors = adj[vertex];
            for (int n : neighbors) {
                if (visited[n]) {
                    continue;
                }
                System.out.print(n + " ");
                queue.add(n);
                visited[n] = true;
            }
        }
    }

    public void BFS(boolean[] visited) {
        for (int v = 0; v < adj.length; v++) {
            if (visited[v]) {
                continue;
            }
            System.out.println("\n------");
            BFS(v, visited);
        }
    }

    public boolean hasPath(int start, int end) {
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        boolean[] visited = new boolean[V];
        while (!q.isEmpty()) {
            int v = q.remove();
            visited[v] = true;
            List<Integer> adjVertices = this.adj[v];
            for (int vx : adjVertices) {
                if (visited[vx]) {
                    continue;
                }
                if (vx == end) {
                    return true;
                }
                q.add(vx);
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(2, 3);

        System.out.println(g.hasPath(2, 0));
    }
}
