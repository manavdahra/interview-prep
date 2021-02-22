package graphs;

import graphs.util.Pair;

import java.util.List;

public class WeightedGraph {
    public int V;
    public List<List<Pair>> adj;

    public WeightedGraph(int v, List<List<Pair>> adj) {
        V = v;
        this.adj = adj;
    }

    public int getV() {
        return V;
    }

    public List<Pair> getNeighbours(int node) {
        return adj.get(node);
    }

    public void setV(int v) {
        V = v;
    }

    public List<List<Pair>> getAdj() {
        return adj;
    }

    public void setAdj(List<List<Pair>> adj) {
        this.adj = adj;
    }
}
