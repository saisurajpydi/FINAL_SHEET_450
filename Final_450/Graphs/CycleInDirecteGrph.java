import java.util.*;

public class CycleInDirecteGrph {
    ArrayList<ArrayList<Integer>> graph;
    int v;

    CycleInDirecteGrph(int node) {
        v = node;
        graph = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < v; i++) {
            graph.add(new ArrayList<Integer>());
        }
    }

    void addEdge(int u, int v) {
        graph.get(u).add(v);
    }

    boolean isCycleUtil(int i, boolean visited[], boolean recStack[]) {
        if (recStack[i])
            return true;

        if (visited[i])
            return false;

        visited[i] = true;

        recStack[i] = true;

        for (int c : graph.get(i))
            if (isCycleUtil(c, visited, recStack))
                return true;

        recStack[i] = false;

        return false;
    }

    boolean isCycle() {
        boolean visited[] = new boolean[v];
        boolean recStack[] = new boolean[v];
        for (int i = 0; i < v; i++)
            if (isCycleUtil(i, visited, recStack))
                return true;

        return false;

    }

    public static void main(String[] args) {
        CycleInDirecteGrph g = new CycleInDirecteGrph(6);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 3);
        g.addEdge(3, 3);
        System.out.println("is Cyclic : " + g.isCycle());
    }
}
