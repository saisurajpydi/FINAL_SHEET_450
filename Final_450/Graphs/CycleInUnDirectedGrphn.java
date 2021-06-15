public class CycleInUnDirectedGrphn {

    class Solution {
        // Function to detect cycle in an undirected graph.
        public boolean isCycle(int v, ArrayList<ArrayList<Integer>> graph) {
            // Code here
            boolean visited[] = new boolean[v];
            for (int i = 0; i < v; i++) {
                visited[i] = false;
            }

            for (int i = 0; i < v; i++) {
                if (!visited[i]) {
                    if (isCycleUtil(i, visited, -1, graph)) {
                        return true;
                    }
                }
            }
            return false;
        }

        boolean isCycleUtil(int i, boolean visited[], int parent, ArrayList<ArrayList<Integer>> graph) {

            visited[i] = true;
            Integer x;
            Iterator<Integer> it = graph.get(i).iterator();
            while (it.hasNext()) {
                x = it.next();
                if (visited[x]) {
                    if (isCycleUtil(x, visited, i, graph)) {
                        return true;
                    }
                } else if (x != parent) {
                    return true;
                }
            }
            return false;
        }
    }
}
