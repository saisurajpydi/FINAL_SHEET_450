import java.util.*;

public class CreateAndPrint {
    ArrayList<ArrayList<Integer>> graph;
    int v;

    CreateAndPrint(int node) {
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

    public static void main(String[] args) {
        CreateAndPrint g = new CreateAndPrint(6);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 3);
        g.addEdge(3, 5);
        g.addEdge(4, 5);
        g.print();
    }
}