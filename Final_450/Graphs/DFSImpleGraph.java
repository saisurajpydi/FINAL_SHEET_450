import java.util.*;

public class DFSImpleGraph {
    ArrayList<ArrayList<Integer>> graph;
    int v;

    DFSImpleGraph(int node) {
        v = node;
        graph = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < v; i++) {
            graph.add(new ArrayList<Integer>());
        }
    }

    void addEdge(int u, int v) {
        graph.get(u).add(v);
        graph.get(v).add(u);
    }

    void print() {
        for (int i = 0; i < v; i++) {
            System.out.print("Node" + i + ":");
            for (int x : graph.get(i)) {
                System.out.print("->" + x);
            }
            System.out.println();
        }
    }

    void dfsUtil(int node, boolean visited[]) {
        visited[node] = true;
        System.out.print(node + " ");
        for (int x : graph.get(node)) {
            if (visited[x] == false) {
                dfsUtil(x, visited);
            }
        }
    }

    void dfs(int start) {
        boolean visited[] = new boolean[v];
        System.out.println("\nDFS traversal is ");
        dfsUtil(start, visited);
    }

    public static void main(String[] args) {
        DFSImpleGraph g = new DFSImpleGraph(6);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 3);
        g.addEdge(3, 5);
        g.addEdge(4, 5);
        g.print();
        g.dfs(0);
    }
}
